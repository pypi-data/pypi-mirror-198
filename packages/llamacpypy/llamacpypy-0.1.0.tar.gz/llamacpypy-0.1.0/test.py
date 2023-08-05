from llamacpypy import Llama

wrap = Llama('models/7B/ggml-model-q4_0.bin', warm_start=False)
wrap.load_model()

var = wrap.generate("This is the weather report, we are reporting a clown fiesta happening at backer street. The clowns ")
print(var)
