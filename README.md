## Environment Setup

1. Open the folder using Visual Studio Code's Remote-Containers extension. Select `From 'Dockerfile'` so the ROS library is configured correctly.
<img src="https://code.visualstudio.com/assets/docs/remote/containers/select-dockerfile.png">

2. Install requirements
```bash
pip3 install -r requirements.txt
```

3. Install the [Microsoft Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

4. You can load Jupyter Notebooks by either opening an `.ipynb` file in VS Code, or running this command to start a Jupyter server:
```bash
jupyter notebook --ip=0.0.0.0 --port=8888
```

5. The Python to interpreter to use if VS Code asks you is `/usr/bin/python3`