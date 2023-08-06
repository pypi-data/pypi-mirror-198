
from urllib.parse import urlparse
from pydantic import BaseModel
from deepmerge import always_merger
import logging, os
from typing import Any

logger = logging.getLogger(__name__)



class Module(BaseModel):
    name: str | None = None
    source: str | None = None
    src: str | None = None
    vars: dict[str, Any] = {}
    providers: list[str] = []   
    stack: Any | None = None

    def __str__(self) -> str:
        return f"<{self.__class__.__name__}:{self.name}@{self.stack.name}>"

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        if self.source:
            self.src = self.source

    @property
    def abssrc(self) -> str:
        return os.path.join(self.stack.cluster.stackd.root, self.src)


    @property
    def charts_root(self) -> str:
        return os.path.join(self.stack.cluster.stackd.root, "charts")

    def get_template(self, template_name):
        return self.stack.cluster.stackd.conf.repos["core"].get_jinja_env().get_template(template_name)

    def write(self, template_name, dest, **kwargs):
        tpl = self.get_template(template_name)
        
        with open(dest, "w") as f:
            f.write(tpl.render(**kwargs))

        logger.debug(f"{self} writed {dest} from {tpl}")

    @property
    def remote_state_template(self) -> str:
        return f"remote_state.s3.hcl.j2"

    @property
    def namespace(self) -> str:
        return f"{self.stack.name}-{self.name}"

    @property
    def cluster_name(self) -> str:
        return self.stack.cluster.name

    @property
    def prefix(self) -> str:
        return f"{self.stack.name}"

    @property
    def ingress_host(self) -> str:
        return f"{self.stack.name}.{self.stack.cluster.name}.{self.stack.cluster.stackd.dns_zone}"

    def get_vars(self, cluster, cluster_stack, **kwargs):
        return dict(
            prefix=self.prefix,
            cluster_name=self.cluster_name,
            cluster=self.cluster_name,
            env=self.cluster_name,
            service=self.name,
            tg_abspath=self.abssrc,
            group="all", # legacy
            environment=self.cluster_name,
            ingress_host=self.ingress_host,
            namespace=self.namespace,
            tf_state_key=f"{self.stack.cluster.name}/{self.namespace}",
            charts_root=self.charts_root,
        )

    def build(self, cluster, cluster_stack, **kwargs):
        path = cluster.stackd.resolve_module_path(self.src)
        dest = os.path.join(cluster.stackd.root, "build", cluster.name,
            self.stack.name, self.name)
        os.makedirs(dest, exist_ok=True)
        vars = always_merger.merge(
            self.get_vars(cluster, cluster_stack, **kwargs),
        always_merger.merge(
            always_merger.merge(cluster.stackd.conf.globals, cluster.globals),
            always_merger.merge(cluster_stack.vars, self.vars)))
        logger.debug(f"vars: {vars}")
        ctx = dict(module=self, cluster=cluster, stackd=cluster.stackd, vars=vars, **kwargs)
        self.write("terragrunt.root.j2", os.path.join(dest, "terragrunt.hcl"), **ctx)        
        self.write("variables.tf.j2", os.path.join(dest, "_variables.tf"), **ctx)
        
        versions = [ v for v in cluster.stackd.versions.values() if v.name in self.providers ]
        self.write("versions.tf.j2", os.path.join(dest, "_versions.tf"), **dict(versions=versions, **ctx))

        self.write("vars.tfvars.json.j2", os.path.join(dest, "vars.tfvars.json"), **dict(versions=versions, **ctx))

        logger.debug(f"{self} building module {self.name} in {self.stack.name} from {path}")

         


class Stack(BaseModel):
    name: str | None = None
    src: str | None = None
    example_vars: dict[str, Any] = {}
    stack: dict[str, Module] = {}
    items: dict[str, Module] = {}
    cluster: Any

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        if self.stack:
            logger.warning(f"stack {self.name} has stack key, this is deprecated, use items instead")
            self.items = self.stack
        
        for module_name, module in self.items.items():
            module.name = module_name
            module.stack = self
        

    def __str__(self) -> str:
        return f"<{self.__class__.__name__}:{self.name}>"


    def build(self, **kwargs):
        for module in self.items.values():
            module.build(**kwargs)