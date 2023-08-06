
import os
from urllib.parse import urlparse
from pydantic import BaseModel, parse_obj_as
import logging
from typing import Any

import yaml

from .stack import Stack

logger = logging.getLogger(__name__)

class ClusterStack(BaseModel):
    name: str | None = None
    src: str | None = None
    vars: dict[str, Any] = {}
    stack: Stack | None = None
    cluster: Any

    def __str__(self) -> str:
        return f"<{self.__class__.__name__}:{self.name}@{self.cluster.name}>"

    def build(self, **kwargs):

        if self.src is None:
            self.src = self.name

        # src is url with repo in scheme
        parsed_src = urlparse(self.src)
        if not parsed_src.scheme:
            parsed_src = urlparse(f"root:{self.src}") # add root repo
        if len(self.src.split("/")) == 1:
            parsed_src = urlparse(f"{parsed_src.scheme}:stack/{self.src}") # add stack dir

        repo = self.cluster.stackd.conf.repos[parsed_src.scheme]

        if self.src.endswith(".yaml"):
            path = os.path.join(repo.repo_dir, parsed_src.path.lstrip("/"))           
        else:
            path = os.path.join(repo.repo_dir, parsed_src.path.lstrip("/"), "stack.yaml")
            

        url = parsed_src.geturl()
        logger.info(f"{self} building stack {self.name} in {self.cluster.name} {url} <- {path}")
        sd = yaml.safe_load(open(path).read())
        sd["name"] = sd.get("name", self.name)
        sd["cluster"] = self.cluster
        self.stack = parse_obj_as(Stack, sd)
        logger.debug(f"{self} stack: {self.stack}")
        self.stack.build(cluster_stack=self, **kwargs)

class Cluster(BaseModel):
    name: str
    globals: dict[str, Any] = {}
    stacks: dict[str, ClusterStack] = {}
    stackd: Any
    

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        for sname, s in self.stacks.items():
            s.cluster = self
            s.name = sname


    def build(self, stack, **kwargs):
        if stack == "all":
            for s in self.stacks.values():
                s.build(cluster=self, **kwargs)
        else:
            s = self.stacks[stack]
            s.build(cluster=self, **kwargs)
        