# explore ways to convert python to webassembly

Status: Redo later

In my mind, I just want to be able to expose python lib functions as web assembly functions.

But you know, this just isn't really possible it appears. If you can use a subset of python, you can maybe compile things to C. See [here](https://stackoverflow.com/a/7112916/4918389). I'm not completely sure how exactly the process looks. Even after reading a fair amount of it it's not clear.

- rustpython
- pyodide
- using facebook's TransCoder to convert python to c++ then go to webassembly
    - on a simple toy example it didn't even make the correct looking code
    - on a real example, I couldn't run it, running into errors like:
    
    ```
    File "/home/jsphweid/TransCoder/XLM/src/model/transformer.py", line 388, in fwd
        tensor = tensor + self.position_embeddings(positions).expand_as(tensor)
    RuntimeError: CUDA error: device-side assert triggered
    ```
    
- convert python to c/c++ code
- [https://us.pycon.org/2016/schedule/presentation/1995/](https://us.pycon.org/2016/schedule/presentation/1995/)
    - project has been dead since this talk in 2016 it appears
- [http://numba.pydata.org/](http://numba.pydata.org/) - explore this!!!!!