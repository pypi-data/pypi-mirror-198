from transformers import AutoConfig, AutoModelForCausalLM

from .configuration_gpt2 import NamiGPT2Config
from .modeling_gpt2 import NamiGPT2LMHeadModel, NamiGPT2LMHeadModelWithValueHead

AutoConfig.register("nami_gpt2", NamiGPT2Config)
AutoModelForCausalLM.register(NamiGPT2Config, NamiGPT2LMHeadModel)
AutoModelForCausalLM.register(NamiGPT2Config, NamiGPT2LMHeadModelWithValueHead)
