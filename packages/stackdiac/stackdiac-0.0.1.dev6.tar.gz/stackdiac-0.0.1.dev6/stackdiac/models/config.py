from pydantic import BaseModel, Field
from typing import Union, Any, List, Optional
import os, logging, git, filecmp, shutil, yaml
from urllib.parse import urlparse
import requests
import io
import zipfile
import time
import os
import stat

from .repo import Repo
from .binary import Binaries, Binary

logger = logging.getLogger(__name__)

class Project(BaseModel):
    name: str
    title: Union[str, None] = None
    vault_address: Union[str, None] = None
    domain: str

class Globals(BaseModel):
    dns_zone: str
    vault_address: str
    tf_state_bucket: str
    project: str


class Config(BaseModel):
    kind: str = "stackd"
    project: Project
    globals: dict
    clusters_dir: str = "clusters"
    repos: dict[str, Repo] = {}
    binaries: Binaries





def get_initial_config(name: str, domain: str, 
    vault_address: Union[str, None], **kwargs) -> Config:
    return Config(
        project = Project(
            name = name,
            domain = domain,
            vault_address = vault_address,
            title = kwargs.get("title", None),
        ),
        globals = dict(
            dns_zone = domain,
            project = name,
            vault_address = vault_address,
            tf_state_bucket = f"{name}-tf-state",
            tf_state_bucket_region = "us-east-1",
            tf_state_backend = "s3",
        ),
        repos = dict(
            root=Repo(
                url="./", local=True,
                name="root", 
                ),
            core=Repo(
                url="https://github.com/stackdiac/core.git",
                #url="../../core", local=True,
                name="core", 
                tag="0.0.1-dev5",
                branch="dev"),

        ),
        binaries = dict(
            terraform = Binary(
                url = "https://releases.hashicorp.com/terraform/1.4.2/terraform_1.4.2_linux_amd64.zip",
                binary = "terraform",
                extract = "terraform",
            ),
            terragrunt = Binary(
                url = "https://github.com/gruntwork-io/terragrunt/releases/download/v0.45.0/terragrunt_linux_amd64",
                binary = "terragrunt",
            ),
        )
    )