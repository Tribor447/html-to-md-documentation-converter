# Quickstart

## Navigation

- [Getting Started](#gettingstarted-quickstart)
  - [Quickstart](#gettingstarted-quickstart)
  - [Jupyter Notebook](#gettingstarted-notebook)
  - [Submarine Python SDK](#gettingstarted-python-sdk)
  - [Custom Configuation](#gettingstarted-helm)
- [User Docs](#userdocs-submarine-sdk-submarine-cli)
  - [Submarine SDK](#userdocs-submarine-sdk-submarine-cli)
    - [Submarine CLI](#userdocs-submarine-sdk-submarine-cli)
    - [Submarine Client](#userdocs-submarine-sdk-submarine-client)
    - [Experiment Client](#userdocs-submarine-sdk-experiment-client)
    - [Tracking](#userdocs-submarine-sdk-tracking)
  - [Others](#userdocs-others-mlflow)
    - [MLflow UI](#userdocs-others-mlflow)
    - [Tensorboard](#userdocs-others-tensorboard)
- [Developer Docs](#devdocs)
  - [Project Architecture](#devdocs)
  - [Dependencies for Submarine](#devdocs-dependencies)
  - [How to Build Submarine](#devdocs-buildfromcode)
  - [Development Guide](#devdocs-development)
  - [How to Run Integration K8s Test](#devdocs-integrationtestk8s)
  - [How to Run Frontend Integration Test](#devdocs-integrationteste2e)
  - [How to Release](#devdocs-howtorelease)
  - [How to Verify](#devdocs-howtoverify)
- [Community](#community)
  - [Apache Submarine Community](#community)
  - [Bylaws](#community-bylaws)
  - [Guide for Apache Submarine Committers](#community-howtocommit)
  - [How To Contribute to Submarine](#community-contributing)
  - [How to vote a Committer or PMC](#community-howtovotecommitterorpmc)
  - [How to become a Committer](#community-howtobecomecommitter)
  - [Resources](#community-resources)
- [Design Docs](#designdocs-architecture-and-requirements)
  - [Architecture and Requirment](#designdocs-architecture-and-requirements)
  - [Implementation Notes](#designdocs-implementation-notes)
  - [Environments Implementation](#designdocs-environments-implementation)
  - [Experiment Implementation](#designdocs-experiment-implementation)
  - [Notebook Implementation](#designdocs-notebook-implementation)
  - [Storage Implementation](#designdocs-storage-implementation)
  - [Submarine Server](#designdocs-submarine-server-architecture)
    - [Submarine Server Implementation](#designdocs-submarine-server-architecture)
    - [Generic Experiment Spec](#designdocs-submarine-server-experimentspec)
  - [WIP Design Docs](#designdocs-wip-designs-submarine-launcher)
    - [Submarine Launcher](#designdocs-wip-designs-submarine-launcher)
    - [Security Implementation](#designdocs-wip-designs-security-implementation)

## Content

<a id="gettingstarted-quickstart"></a>

<!-- source_url: https://submarine.apache.org/docs/gettingStarted/quickstart/ -->

<!-- page_index: 1 -->

# Quickstart

Version: 0.8.0

This document gives you a quick view on the basic usage of Submarine platform. You can finish each step of ML model lifecycle on the platform without messing up with the troublesome environment problems.

1. Prerequisite

- Check [dependency page](#devdocs-dependencies) for the compatible version
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [helm](https://helm.sh/docs/intro/install/) (Helm v3 is minimum requirement.)
- [minikube](https://minikube.sigs.k8s.io/docs/start/).
- [istioctl](https://istio.io/latest/docs/setup/getting-started/#download)

2. Start minikube cluster and install Istio

Start minikube

```bash
# You can go to https://minikube.sigs.k8s.io/docs/start/ and follow the tutorial to install minikube.
# Then you can start kubernetes with minikube:minikube start --vm-driver=docker --cpus 8 --memory 8192 --kubernetes-version v1.24.12
 
# The version of k8s can be adjusted to the range of your current minikube.
# For example, minikube v1.28.0 can provide versions from v1.25.0 to v1.25.3 in k8s 1.25
 
# Or if you want to support Pod Security Policy (https://minikube.sigs.k8s.io/docs/tutorials/using_psp) in k8s 1.21 or 1.22, you can use the following command to start cluster minikube start --extra-config=apiserver.enable-admission-plugins=PodSecurityPolicy --addons=pod-security-policy --vm-driver=docker --cpus 8 --memory 8192 --kubernetes-version v1.21.2
```

Install Istio, there are two ways to install: Command-Istioctl-based, or Helm-based

```bash
# You can go to the https://github.com/istio/istio/releases/ to download the istioctl for your k8s version
# e.g. we can execute the following command to download the istio version adapted to k8s 1.24.12
# wget https://github.com/istio/istio/releases/download/1.17.1/istio-1.17.1-linux-amd64.tar.gz istioctl install -y
 
# Alternatively, you can use istio's helm to install
# This is the link: https://istio.io/latest/docs/setup/install/helm/## Add istio repo helm repo add istio https://istio-release.storage.googleapis.com/charts helm repo update ## Create istio-system namespace kubectl create namespace istio-system ## Install istio resources helm install istio-base istio/base -n istio-system helm install istiod istio/istiod -n istio-system helm install istio-ingressgateway istio/gateway -n istio-system
```

1. Clone the project

```bash
git clone https://github.com/apache/submarine.git 
cd submarine 
```

2. Create necessary namespaces

```bash
# create namespace for submarine, training, notebook and seldon-core operators kubectl create namespace submarine kubectl label namespace submarine istio-injection=enabled
 
# create namespace for deploying submarine-server kubectl create namespace submarine-user-test kubectl label namespace submarine-user-test istio-injection=enabled
 
# After k8s 1.25, we can turn on PSA (Pod Security Admission) labels for namespace.
# We use a common PSA enforcement level. If you want to use a more detailed configuration, you can refer to
# https://kubernetes.io/docs/concepts/security/pod-security-admission/#pod-security-admission-labels-for-namespaces kubectl label namespace submarine-user-test 'pod-security.kubernetes.io/enforce=privileged'
```

3. Install the submarine operator and dependencies by helm chart

```bash
# Update helm dependency. helm dependency update ./helm-charts/submarine
# Install submarine operator in namespace submarine. helm install submarine ./helm-charts/submarine --set seldon-core-operator.istio.gateway=submarine/seldon-gateway -n submarine
```

4. Create a Submarine custom resource and the operator will create the submarine server, database, etc. for us.

```bash
kubectl apply -f submarine-cloud-v3/config/samples/_v1_submarine.yaml -n submarine-user-test 
```

```bash
$ kubectl get pods -n submarine NAME READY STATUS RESTARTS AGE notebook-controller-deployment-66d85984bf-x562z 1/1 Running 0 7h7m training-operator-6dcd5b9c64-nxwr2 1/1 Running 0 7h7m submarine-operator-9cb7bc84d-brddz 1/1 Running 0 7h7m
 
$ kubectl get pods -n submarine-user-test NAME READY STATUS RESTARTS AGE submarine-database-0 1/1 Running 0 7h6m submarine-minio-686b8777ff-zg4d2 2/2 Running 0 7h6m submarine-mlflow-68c5559dcb-lkq4g 2/2 Running 0 7h6m submarine-server-7c6d7bcfd8-5p42w 2/2 Running 0 9m33s submarine-tensorboard-57c5b64778-t4lww 2/2 Running 0 7h6m
```

1. Exposing service

```bash
kubectl port-forward --address 0.0.0.0 -n istio-system service/istio-ingressgateway 32080:80 
```

2. View workbench

Go to `http://0.0.0.0:32080`
![](assets/images/quickstart-worbench-0d8c2f6217f22460d4cf8e9b05d06f6b_a0766d34bb8102d6.png)

We put the code of this example [here](https://github.com/apache/submarine/tree/master/dev-support/examples/quickstart). `train.py` is our training script, and `build.sh` is the script to build a docker image.

Take a simple mnist tensorflow script as an example. We choose `MultiWorkerMirroredStrategy` as our distributed strategy.

```python
""" 
./dev-support/examples/quickstart/train.py 
Reference: https://github.com/kubeflow/training-operator/blob/master/examples/tensorflow/distribution_strategy/keras-API/multi_worker_strategy-with-keras.py 
""" 
 
import tensorflow as tf 
import tensorflow_datasets as tfds 
from packaging.version import Version 
from tensorflow.keras import layers, models 
 
import submarine 
 
 
def make_datasets_unbatched(): 
    BUFFER_SIZE = 10000 
 
    # Scaling MNIST data from (0, 255] to (0., 1.] 
    def scale(image, label): 
        image = tf.cast(image, tf.float32) 
        image /= 255 
        return image, label 
 
    # If we use tensorflow_datasets > 3.1.0, we need to disable GCS 
    # https://github.com/tensorflow/datasets/issues/2761#issuecomment-1187413141 
    if Version(tfds.__version__) > Version("3.1.0"): 
        tfds.core.utils.gcs_utils._is_gcs_disabled = True 
    datasets, _ = tfds.load(name="mnist", with_info=True, as_supervised=True) 
 
    return datasets["train"].map(scale).cache().shuffle(BUFFER_SIZE) 
 
 
def build_and_compile_cnn_model(): 
    model = models.Sequential() 
    model.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1))) 
    model.add(layers.MaxPooling2D((2, 2))) 
    model.add(layers.Conv2D(64, (3, 3), activation="relu")) 
    model.add(layers.MaxPooling2D((2, 2))) 
    model.add(layers.Conv2D(64, (3, 3), activation="relu")) 
    model.add(layers.Flatten()) 
    model.add(layers.Dense(64, activation="relu")) 
    model.add(layers.Dense(10, activation="softmax")) 
 
    model.summary() 
 
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]) 
 
    return model 
 
 
def main(): 
    strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy( 
        communication=tf.distribute.experimental.CollectiveCommunication.AUTO 
    ) 
 
    BATCH_SIZE_PER_REPLICA = 4 
    BATCH_SIZE = BATCH_SIZE_PER_REPLICA * strategy.num_replicas_in_sync 
 
    with strategy.scope(): 
        ds_train = make_datasets_unbatched().batch(BATCH_SIZE).repeat() 
        options = tf.data.Options() 
        options.experimental_distribute.auto_shard_policy = ( 
            tf.data.experimental.AutoShardPolicy.DATA 
        ) 
        ds_train = ds_train.with_options(options) 
        # Model building/compiling need to be within `strategy.scope()`. 
        multi_worker_model = build_and_compile_cnn_model() 
 
    class MyCallback(tf.keras.callbacks.Callback): 
        def on_epoch_end(self, epoch, logs=None): 
            # monitor the loss and accuracy 
            print(logs) 
            submarine.log_metric("loss", logs["loss"], epoch) 
            submarine.log_metric("accuracy", logs["accuracy"], epoch) 
 
    multi_worker_model.fit(ds_train, epochs=10, steps_per_epoch=70, callbacks=[MyCallback()]) 
    # save model 
    submarine.save_model(multi_worker_model, "tensorflow") 
 
 
if __name__ == "__main__": 
    main() 
 
```

Build a docker image equipped with the requirement of the environment.

```bash
eval $(minikube docker-env) 
./dev-support/examples/quickstart/build.sh 
```

1. Open submarine workbench and click `+ New Experiment`
2. Choose `Define your experiment`
3. Fill the form accordingly. Here we set 3 workers.

   1. Step 1
      ![](assets/images/quickstart-submit-1-0-7-0-cec455a03933cc7b038a35a141a743b9_c528bd5c6876e291.png)
   2. Step 2
      ![](assets/images/quickstart-submit-2-0-7-0-2bce3b75c9f7c0ee0f44ee9b2bdb742e_9bdc4563a83dd088.png)
   3. Step 3
      ![](assets/images/quickstart-submit-3-0-7-0-f7f3107669746b2c2a58e0794051a24b_b224cc4781fae229.png)
   4. The experiment is successfully submitted
      ![](assets/images/quickstart-submit-4-0-7-0-34946a5790013de952eb32d1246f4a23_4807fa816b569f81.png)
4. In the meantime, we have built this image in docker hub and you can run this experiment directly if you choose `quickstart` in `From predefined experiment library`.

1. In our code, we use `submarine` from `submarine-sdk` to record the metrics. To see the result, click corresponding experiment with name `mnist-example` in the workbench.
2. To see the metrics of each worker, you can select a worker from the left top list.

![](assets/images/quickstart-ui-0-7-0-821f5ad73116d9a9d3088cddcb576836_60352fd08f2620bd.png)

1. Before serving, we need to register a new model.

![](assets/images/submarine-register-model-6540e8f76744c0f1e84013e7e6d78341_a655207cd42d5e9e.png)

2. And then, check the output model in experiment page.

![](assets/images/quickstart-artifacts-31b0ede0bd1f74695a266b185c70c1f1_0fa19bb729e0c53e.png)

3. Click the button and register the model.

![](assets/images/submarine-register-model-6540e8f76744c0f1e84013e7e6d78341_a655207cd42d5e9e.png)

4. Go to the model page and deploy our model for serving.

![](assets/images/submarine-serve-model-37ce5e2709d59223d7a7461ecd4f90d1_3d17884635f2c871.png)

5. We can run the following commands to get the `VirtualService` and `Endpoint` that use istio for external port forward or ingress.

```bash
## get VirtualService with your model name 
kubectl describe VirtualService -n submarine-user-test -l model-name=tf-mnist 
 
Name:         submarine-model-1-2508dd65692740b18ff5c6c6c162b863 
Namespace:    submarine-user-test 
Labels:       model-id=2508dd65692740b18ff5c6c6c162b863 
              model-name=tf-mnist 
              model-version=1 
Annotations:  <none> 
API Version:  networking.istio.io/v1beta1 
Kind:         VirtualService 
Metadata: 
  Creation Timestamp:  2022-09-18T05:26:38Z 
  Generation:          1 
  Managed Fields: 
    ... 
Spec: 
  Gateways: 
    submarine/seldon-gateway 
  Hosts: 
    * 
  Http: 
    Match: 
      Uri: 
        Prefix:  /seldon/submarine-user-test/1/1/ 
    Rewrite: 
      Uri:  / 
    Route: 
      Destination: 
        Host:  submarine-model-1-2508dd65692740b18ff5c6c6c162b863 
        Port: 
          Number:  8000 
Events:            <none> 
```

To confirm that the serving endpoint is available, try using the swagger address to confirm the availability of the interface.
In our example, the address of the swagger is: http://localhost:32080/seldon/submarine-user-test/1/1/api/v1.0/doc/

More details can be found in the official seldon documentation: <https://docs.seldon.io/projects/seldon-core/en/latest/workflow/serving.html#generated-documentation-swagger-ui>

6. After successfully serving the model, we can test the results of serving using the test python code [serve\_predictions.py](https://github.com/apache/submarine/blob/master/dev-support/examples/quickstart/serve_predictions.py)

![](assets/images/submarine-serve-prediction-c6038a5bfd49f11d234ba11442618067_2490128337a487ce.png)

---

<a id="gettingstarted-notebook"></a>

<!-- source_url: https://submarine.apache.org/docs/gettingStarted/notebook/ -->

<!-- page_index: 2 -->

# Jupyter Notebook

Version: 0.8.0

This guide describes how to use Jupyter notebook in Submarine to launch
and manage Jupyter notebooks.

We recommend using Web UI to manage notebooks.

Notebooks can be started from the Web UI. You can click the “Notebook” tab in the
left-hand panel to manage your notebooks.

![](assets/images/notebook-list-0-7-0-dbbd48731a237cca69899bbf68f85570_bf7ce85acabe59f2.png)

To create a new notebook server, click “New Notebook”. You should see a form for entering
details of your new notebook server.

- Notebook Name : Name of the notebook server. It should follow the rules below.
  1. Contain at most 63 characters.
  2. Contain only lowercase alphanumeric characters or '-'.
  3. Start with an alphabetic character.
  4. End with an alphanumeric character.
- Environment : It defines a set of libraries and docker image.
- CPU and Memory
- GPU (optional)
- EnvVar (optional) : Injects environment variables into the notebook.

If you want to use notebook-gpu-env, you should set up the gpu environment in your kubernetes.
You can install [NVIDIA/k8s-device-plugin](https://github.com/NVIDIA/k8s-device-plugin).
The list of prerequisites for running the NVIDIA device plugin is described below

- NVIDIA drivers ~= 384.81
- nvidia-docker version > 2.0
- docker configured with nvidia as the default runtime
- Kubernetes version >= 1.10

**If you’re not sure which environment you need, please choose the environment “notebook-env”
for the new notebook.**

![](assets/images/notebook-form-0-7-0-682e8b09582336c37b0f1e18685824ab_37573e5181115e51.png)

You should see your new notebook server. Click the name of your notebook server to connect to it.

![](assets/images/created-notebook-0-7-0-73ecae05703e406a083d3791c20d19c0_39fde596dd827a99.png)

The environment “notebook-env” includes Submarine Python SDK which can talk to Submarine Server to
create experiments, as the example below:

```python
from __future__ import print_function 
import submarine 
from submarine.client.models.environment_spec import EnvironmentSpec 
from submarine.client.models.experiment_spec import ExperimentSpec 
from submarine.client.models.experiment_task_spec import ExperimentTaskSpec 
from submarine.client.models.experiment_meta import ExperimentMeta 
from submarine.client.models.code_spec import CodeSpec 
 
# Create Submarine Client 
submarine_client = submarine.ExperimentClient() 
 
# Define TensorFlow experiment spec 
environment = EnvironmentSpec(image='apache/submarine:tf-dist-mnist-test-1.0') 
experiment_meta = ExperimentMeta(name='mnist-dist', 
                                 namespace='default', 
                                 framework='Tensorflow', 
                                 cmd='python /var/tf_dist_mnist/dist_mnist.py --train_steps=100', 
                                 env_vars={'ENV1': 'ENV1'}) 
 
worker_spec = ExperimentTaskSpec(resources='cpu=1,memory=1024M', 
                                 replicas=1) 
ps_spec = ExperimentTaskSpec(resources='cpu=1,memory=1024M', 
                                 replicas=1) 
code_spec = CodeSpec(sync_mode="git", git=GitCodeSpec(url="https://github.com/apache/submarine.git")) 
 
experiment_spec = ExperimentSpec(meta=experiment_meta, 
                                 environment=environment, 
                                 code=code_spec, 
                                 spec={'Ps' : ps_spec,'Worker': worker_spec}) 
 
# Create experiment 
experiment = submarine_client.create_experiment(experiment_spec=experiment_spec) 
 
```

You can create a new notebook, paste the above code and run it. Or, you can find the notebook [`submarine_experiment_sdk.ipynb`](https://github.com/apache/submarine/blob/master/submarine-sdk/pysubmarine/example/submarine_experiment_sdk.ipynb) inside the launched notebook session. You can open it, try it out.

After experiment submitted to Submarine server, you can find the experiment jobs on the UI.

---

<a id="gettingstarted-python-sdk"></a>

<!-- source_url: https://submarine.apache.org/docs/gettingStarted/python-sdk/ -->

<!-- page_index: 3 -->

# Submarine Python SDK

Version: 0.8.0

Submarine Python SDK can runs on any machine and it will talk to Submarine Server via REST API. So you can install Submarine Python SDK on your laptop, a gateway machine, your favorite IDE (like PyCharm/Jupyter, etc.).

Furthermore, Submarine supports an extensible package of CTR models based on **TensorFlow** and **PyTorch** along with lots of core components layers that can be used to easily build custom models. You can train any model with `model.train()` and `model.predict()`.

Submarine SDK requires Python3.7+.
It's better to use a new Python environment created by `Anoconda` or Python `virtualenv` to try this to avoid trouble to existing Python environment.
A sample Python virtual env can be setup like this:

```bash
wget https://files.pythonhosted.org/packages/33/bc/fa0b5347139cd9564f0d44ebd2b147ac97c36b2403943dbee8a25fd74012/virtualenv-16.0.0.tar.gz 
tar xf virtualenv-16.0.0.tar.gz 
 
# Make sure to install using Python 3 python3 virtualenv-16.0.0/virtualenv.py venv. venv/bin/activate
```

Starting from `0.4.0`, Submarine provides Python SDK. Please change it to a proper version needed.

More detail: <https://pypi.org/project/apache-submarine/>

```bash
# Install latest stable version pip install apache-submarine
# Install specific version pip install apache-submarine==<REPLACE_VERSION>
```

Please first clone code from github or go to `http://submarine.apache.org/download.html` to download released source code.

```bash
git clone https://github.com/apache/submarine.git 
# (optional) chackout specific branch or release git checkout <correct release tag/branch> cd submarine/submarine-sdk/pysubmarine pip install .
```

Assuming you've installed submarine on K8s and forward the traefik service to localhost, now you can open a Python shell, Jupyter notebook or any tools with Submarine SDK installed.

Follow [SDK experiment example](https://github.com/apache/submarine/blob/master/submarine-sdk/pysubmarine/example/submarine_experiment_sdk.ipynb) to run an experiment.

The Submarine also supports users to train an easy-to-use CTR model with a few lines of code and a configuration file, so they don’t need to reimplement the model by themself. In addition, they can train the model on both local on distributed systems, such as Hadoop or Kubernetes.

Follow [SDK DeepFM example](https://github.com/apache/submarine/blob/master/submarine-sdk/pysubmarine/example/deepfm_example.ipynb) to try the model.

---

<a id="gettingstarted-helm"></a>

<!-- source_url: https://submarine.apache.org/docs/gettingStarted/helm/ -->

<!-- page_index: 4 -->

# Custom Configuation

Version: 0.8.0

Submarine can support various [volume types](https://kubernetes.io/docs/concepts/storage/volumes/#nfs), currently including hostPath (default) and NFS. It can be easily configured in the `./helm-charts/submarine/values.yaml`, or you can override the default values in `values.yaml` by [helm CLI](https://helm.sh/docs/helm/helm_install/).

- In hostPath, you can store data directly in your node.
- Usage:
  1. Configure setting in `./helm-charts/submarine/values.yaml`.
  2. To enable hostPath storage, set `.storage.type` to `host`.
  3. To set the root path for your storage, set `.storage.host.root` to `<any-path>`
- Example:


```yaml
# ./helm-charts/submarine/values.yaml 
storage: 
  type: host 
  host: 
    root: /tmp 
```

- In NFS, it allows multiple clients to access a shared space.
- Prerequisite:
  1. A pre-existing NFS server. You have two options.
     1. Create NFS server


```bash
kubectl create -f ./dev-support/nfs-server/nfs-server.yaml 
```

        It will create a nfs-server pod in kubernetes cluster, and expose nfs-server ip at `10.96.0.2`
     2. Use your own NFS server
  2. Install NFS dependencies in your nodes
     - Ubuntu


```bash
apt-get install -y nfs-common 
```

     - CentOS


```bash
yum install nfs-util 
```

- Usage:
  1. Configure setting in `./helm-charts/submarine/values.yaml`.
  2. To enable NFS storage, set `.storage.type` to `nfs`.
  3. To set the ip for NFS server, set `.storage.nfs.ip` to `<any-ip>`
- Example:


```yaml
# ./helm-charts/submarine/values.yaml 
storage: 
  type: nfs 
  nfs: 
    ip: 10.96.0.2 
```

Submarine server by default expose 8080 port within K8s cluster. After Submarine v0.5
uses Traefik as reverse-proxy by default. If you don't want to
use Traefik, you can modify below value to ***false*** in `./helm-charts/submarine/values.yaml`.

```yaml
# Use Traefik by default 
traefik: 
  enabled: true 
```

To access the server from outside of the cluster, we use Traefik ingress controller and
NodePort for external access.\
Please refer to `./helm-charts/submarine/charts/traefik/values.yaml` and [Traefik docs](https://docs.traefik.io/)
for more details if you want to customize the default value for Traefik.

*Notice:*
If you use `kind` to run local Kubernetes cluster, please refer to this [docs](https://kind.sigs.k8s.io/docs/user/configuration/#extra-port-mappings)
and set the configuration "extraPortMappings" when creating the k8s cluster.

```text
kind: Cluster 
apiVersion: kind.x-k8s.io/v1alpha4 
nodes: 
- role: control-plane 
  extraPortMappings: 
  - containerPort: 32080 
    hostPort: [the port you want to access] 
```

```text
# Use nodePort and Traefik ingress controller by default. 
# To access the submarine server, open the following URL in your browser. 
http://127.0.0.1:32080 
```

If minikube is installed, use the following command to find the URL to the Submarine server.

```text
$ minikube service submarine-traefik --url 
```

To deploy Dashboard, execute the following command:

```text
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-beta8/aio/deploy/recommended.yaml 
```

Run the following commands to grant the cluster access permission of dashboard:

```text
kubectl create serviceaccount dashboard-admin-sa 
kubectl create clusterrolebinding dashboard-admin-sa --clusterrole=cluster-admin --serviceaccount=default:dashboard-admin-sa 
```

If you want to use the token to login the dashboard, run the following commands to get key:

```text
kubectl get secrets 
# select the right dashboard-admin-sa-token to describe the secret 
kubectl describe secret dashboard-admin-sa-token-6nhkx 
```

```text
kubectl proxy 
```

Now access Dashboard at:

> http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/

Dashboard screenshot:

![](assets/images/kind-dashboard-96b734dca17dd1d6043efad54f4c4725_497db389d4b4ffbe.png)

---

<a id="userdocs-submarine-sdk-submarine-cli"></a>

<!-- source_url: https://submarine.apache.org/docs/userDocs/submarine-sdk/submarine-cli/ -->

<!-- page_index: 5 -->

# Submarine CLI

Version: 0.8.0

Submarine CLI comes with pysubmarine python package. You can get CLI tools by pip installing apache-submarine.

You can set your CLI settings by this command

```bash
submarine config init  
```

Return

```bash
Submarine CLI Config initialized 
```

Restore CLI config to default (hostname=`localhost`,port=`32080`)

```bash
submarine config list  
```

For example : return

```bash
╭──────────────────── SubmarineCliConfig ─────────────────────╮ 
│ {                                                           │ 
│   "connection": {                                           │ 
│     "hostname": "localhost",                                │ 
│     "port": 32080                                           │ 
│   }                                                         │ 
│ }                                                           │ 
╰─────────────────────────────────────────────────────────────╯ 
```

```bash
submarine config set <parameter_path> <value>  
```

For example, Set connection port to 8080:

```bash
submarine config set connection.port 8080 
```

```bash
submarine config get <parameter_path> 
```

For example,

```bash
submarine config get connection.port 
```

Return

```bash
connection.port=8080 
```

```bash
submarine list notebook  
```

```bash
submarine get notebook <notebook id> 
```

> you can get notebook id by using `list command`

```bash
submarine delete notebook <notebook id> 
```

```bash
submarine list experiment  
```

```bash
submarine get experiment <experiment id> 
```

> you can get experiment id by using `list command`

```bash
submarine delete experiment <experiment id> [--wait/--no-wait] 
```

- --wait/--no-wait: blocking or non blocking (default no wait)

```bash
submarine list environment  
```

```bash
submarine get environment <environment name> 
```

```bash
submarine delete experiment <environment name> 
```

---

<a id="userdocs-submarine-sdk-submarine-client"></a>

<!-- source_url: https://submarine.apache.org/docs/userDocs/submarine-sdk/submarine-client/ -->

<!-- page_index: 6 -->

# Submarine Client

Version: 0.8.0

Client of submarine to log metric/param, save model and create/delete serve.

Log a single key-value metric with job id and worker index. The value must always be a number.

| Param | Type | Description | Default Value |
| --- | --- | --- | --- |
| job\_id | String | The job name to which the metric should be logged. | x |
| key | String | Metric name. | x |
| value | Float | Metric worker\_index. | x |
| worker\_index | String | Parameter worker\_index. | x |
| timestamp | Datetime | Time when this metric was calculated. Defaults to the current system time. | datetime.now() |
| step | Integer | A single integer step at which to log the specified Metrics, by default it's 0. | 0 |

Log a single key-value parameter with job id and worker index. The key and value are both strings.

| Param | Type | Description | Default Value |
| --- | --- | --- | --- |
| job\_id | String | The job name to which the parameter should be logged. | x |
| key | String | Parameter name. | x |
| value | String | Parameter value. | x |
| worker\_index | String | Parameter worker\_index. | x |

Save a model into the minio pod.

| Param | Type | Description | Default Value |
| --- | --- | --- | --- |
| model | Object | Model artifact. | x |
| model\_type | String | Version of a registered model. | x |
| registered\_model\_name | String | If it is not `None`, the model will be registered into the model registry with this name. | None |
| input\_dim | List<String> | The input dimension of the model. | None |
| output\_dim | List<String> | The output dimension of the model. | None |

Create serve of a model through Seldon Core.

| Param | Type | Description | Default Value |
| --- | --- | --- | --- |
| model\_name | String | Name of a registered model. | x |
| model\_version | Integer | Version of a registered model. | x |
| async\_req | Boolean | Execute request asynchronously. | True |

**Returns**
Return a dictionary with inference url.

Delete a serving model.

| Param | Type | Description | Default Value |
| --- | --- | --- | --- |
| model\_name | String | Name of a registered model. | x |
| model\_version | Integer | Version of a registered model. | x |
| async\_req | Boolean | Execute request asynchronously. | True |

---

<a id="userdocs-submarine-sdk-experiment-client"></a>

<!-- source_url: https://submarine.apache.org/docs/userDocs/submarine-sdk/experiment-client/ -->

<!-- page_index: 7 -->

# Experiment Client

Version: 0.8.0

Client of a submarine server that creates and manages experients and logs.

Create an experiment.

| Param | Type | Description | Default Value |
| --- | --- | --- | --- |
| experiment\_spec | Dict | Submarine experiment spec. More detailed information can be found at [Experiment API](https://submarine.apache.org/docs/api/experiment) | x |

**Returns**

The detailed info about the submarine experiment.

**Example**

```python
from submarine import * client = ExperimentClient() client.create_experiment({"meta": {"name": "tf-mnist-json","namespace": "default","framework": "TensorFlow","cmd": "python /var/tf_mnist/mnist_with_summaries.py --log_dir=/train/log --learning_rate=0.01 --batch_size=150","envVars": {"ENV_1": "ENV1"} },"environment": {"image": "apache/submarine:tf-mnist-with-summaries-1.0" },"spec": {"Ps": {"replicas": 1,"resources": "cpu=1,memory=1024M" },"Worker": {"replicas": 1,"resources": "cpu=1,memory=1024M"}} })
```

Patch an experiment.

| Param | Type | Description | Default Value |
| --- | --- | --- | --- |
| id | String | Submarine experiment id. | x |
| experiment\_spec | Dict | Submarine experiment spec. More detailed information of Submarine experiment spec can be found at [Experiment API](https://submarine.apache.org/docs/api/experiment). | x |

**Returns**

The detailed info about the submarine experiment.

**Example**

```python
client.patch_experiment("experiment_1626160071451_0008", {"meta": {"name": "tf-mnist-json","namespace": "default","framework": "TensorFlow","cmd": "python /var/tf_mnist/mnist_with_summaries.py --log_dir=/train/log --learning_rate=0.01 --batch_size=150","envVars": {"ENV_1": "ENV1"} },"environment": {"image": "apache/submarine:tf-mnist-with-summaries-1.0" },"spec": {"Worker": {"replicas": 2,"resources": "cpu=1,memory=1024M"}} })
```

Get the experiment's detailed info by id.

| Param | Type | Description | Default Value |
| --- | --- | --- | --- |
| id | String | Submarine experiment id. | x |

**Returns**

The detailed info about the submarine experiment.

**Example**

```python
experiment = client.get_experiment("experiment_1626160071451_0008") 
```

List all experiment for the user.

| Param | Type | Description | Default Value |
| --- | --- | --- | --- |
| status | Optional[str] | Accepted, Created, Running, Succeeded, Deleted. | None |

**Returns**

List of submarine experiments.

**Example**

```python
experiments = client.list_experiments() 
```

Delete the submarine experiment.

| Param | Type | Description | Default Value |
| --- | --- | --- | --- |
| id | String | Submarine experiment id. | x |

**Returns**

The detailed info about the deleted submarine experiment.

**Example**

```python
client.delete_experiment("experiment_1626160071451_0008") 
```

Print training logs of all pod of the experiment.
By default print all the logs of Pod.

| Param | Type | Description | Default Value |
| --- | --- | --- | --- |
| id | String | Submarine experiment id. | x |
| onlyMaster | Optional[bool] | By default include pod log of "master" which might be Tensorflow PS/Chief or PyTorch master. | x |

**Return**

- The info of pod logs

**Example**

```python
client.get_log("experiment_1626160071451_0009") 
```

List experiment log.

| Param | Type | Description | Default Value |
| --- | --- | --- | --- |
| status | String | Accepted, Created, Running, Succeeded, Deleted. | x |

**Returns**

List of submarine experiment logs.

Example

```python
logs = client.list_log("Succeeded") 
```

Waits until the experiment is finished or failed.

| Param | Type | Description | Default Value |
| --- | --- | --- | --- |
| id | String | Submarine experiment id. | x |
| polling\_interval | Optional[int] | How many seconds between two polls for the status of the experiment. | 10 |

**Returns**

Submarine experiment logs.

**Example**

```python
logs = client.wait_for_finish("experiment_1626160071451_0009", 5) 
```

---

<a id="userdocs-submarine-sdk-tracking"></a>

<!-- source_url: https://submarine.apache.org/docs/userDocs/submarine-sdk/tracking/ -->

<!-- page_index: 8 -->

# Tracking

Version: 0.8.0

It helps developers use submarine's internal data caching, data exchange, and task tracking capabilities to more efficiently improve the
development and execution of machine learning productivity

- Allow data scientist to track distributed ML experiment
- Support store ML parameters and metrics in Submarine-server
- Support hdfs, S3 and mysql (Currently we only support mysql)

Get the tracking URI. If none has been specified, check the environmental variables. If uri is still none, return the default submarine jdbc url.

**Returns**

The tracking URI.

set the tracking URI. You can also set the SUBMARINE\_TRACKING\_URI environment variable to have Submarine find a URI from there. The URI should be database connection string.

| Param | Type | Description | Default Value |
| --- | --- | --- | --- |
| uri | String | Submarine record data to Mysql server. The database URL is expected in the format `<dialect>+<driver>://<username>:<password>@<host>:<port>/<database>`.By default it's `mysql+pymysql://submarine:password@submarine-database:3306/submarine`. More detail : [SQLAlchemy docs](https://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls) | x |

log a single key-value parameter. The key and value are both strings.

| Param | Type | Description | Default Value |
| --- | --- | --- | --- |
| key | String | Parameter name. | x |
| value | String | Parameter value. | x |

log a single key-value metric. The value must always be a number.

| Param | Type | Description | Default Value |
| --- | --- | --- | --- |
| key | String | Metric name. | x |
| value | Float | Metric value. | x |
| step | Integer | A single integer step at which to log the specified Metrics. | 0 |

Save a model into the minio pod.

| Param | Type | Description | Default Value |
| --- | --- | --- | --- |
| model\_type | String | The type of model. Only support `pytorch` and `tensorflow`. | x |
| model | Object | Model artifact. | x |
| registered\_model\_name | String | If it is not `None`, the model will be registered into the model registry with this name. | None |
| input\_dim | List<Integer> | The input dimension of the model. | None |
| output\_dim | List<Integer> | The output dimension of the model. | None |

---

<a id="userdocs-others-mlflow"></a>

<!-- source_url: https://submarine.apache.org/docs/userDocs/others/mlflow/ -->

<!-- page_index: 9 -->

# MLflow UI

Version: 0.8.0

MLflow UI shows the tracking result of the experiments. When we
use the log\_param or log\_metric in ModelClient API, we could view
the result in MLflow UI. Below is the example of the usage of MLflow
UI.

1. Run the following code in the cluster

```python
from submarine import ModelsClient 
import random 
import time 
 
if __name__ == "__main__": 
  modelClient = ModelsClient() 
  with modelClient.start() as run: 
      modelClient.log_param("learning_rate", random.random()) 
      for i in range(100): 
        time.sleep(1) 
        modelClient.log_metric("mse", random.random() * 100, i) 
        modelClient.log_metric("acc", random.random(), i) 
```

2. In the MLflow UI page, you can see the log\_param and the log\_metric
   result. You can also compare the training between different workers.

![](assets/images/mlflow-ui-e2fbae31ba60c324e66f00f0ae3caebf_616348e1e9f1f046.png)

---

<a id="userdocs-others-tensorboard"></a>

<!-- source_url: https://submarine.apache.org/docs/userDocs/others/tensorboard/ -->

<!-- page_index: 10 -->

# Tensorboard

Version: 0.8.0

- `SUBMARINE_TENSORBOARD_LOG_DIR`: Exist in every experiment container. You just need to direct your logs to `$(SUBMARINE_TENSORBOARD_LOG_DIR)` (**NOTICE: it is `()` not `{}`**), and you can inspect the process on the tensorboard webpage.

```text
{"meta": {"name": "tensorflow-tensorboard-dist-mnist","namespace": "default","framework": "TensorFlow","cmd": "python /var/tf_mnist/mnist_with_summaries.py --log_dir=$(SUBMARINE_TENSORBOARD_LOG_DIR) --learning_rate=0.01 --batch_size=20","envVars": {"ENV_1": "ENV1"} },"environment": {"image": "apache/submarine:tf-mnist-with-summaries-1.0" },"spec": {"Worker": {"replicas": 1,"resources": "cpu=1,memory=512M"}}}
```

1. Open the experiment page in the workbench, and Click the `TensorBoard` button.

![](assets/images/tensorboard-experiment-page-bf5d5aad633d80ef059ce4b7e4d91db3_57922dab0ef3c6e0.png)

2. Inspect the process on tensorboard page.

![](assets/images/tensorboard-webpage-f8b9c5ceeb7b5ef535939ea22f680d96_9eeb2e0ccabfef68.png)

---

<a id="devdocs"></a>

<!-- source_url: https://submarine.apache.org/docs/devDocs/ -->

<!-- page_index: 11 -->

# Project Architecture

Version: 0.8.0

This document mainly describes the structure of each module of the Submarine project, the development and test description of each module.

Provide the CLI interface for submarine user. (Currently only support YARN service (deprecated))

The operator for Submarine application. For details, please see the [README on github](https://github.com/apache/submarine/blob/master/submarine-cloud-v2/README.md).

Define utility function used in multiple packages, mainly related to hadoop.

Store the pre-release files.

Provide Python SDK for submarine user.

Include core server, restful api, and k8s submitter.

Provide end-to-end and k8s test for submarine.

- workbench-server: is a Jetty-based web server service. Workbench-server provides RESTful interface and Websocket interface. The RESTful interface provides workbench-web with management capabilities for databases such as project, department, user, and role.
- workbench-web: is a web front-end service based on Angular.js framework. With workbench-web users can manage Submarine project, department, user, role through browser. You can also use the notebook to develop machine learning algorithms, model release and other lifecycle management.

- **mini-submarine**: by using the docker image provided by Submarine, you can
  experience all the functions of Submarine in a single docker environment, while
  mini-submarine also provides developers with a development and testing
  environment, Avoid the hassle of installing and deploying the runtime
  environment.
- **submarine-installer**: submarine-installer is our submarine runtime
  environment installation tool for yarn-3.1+ and above.By using
  submarine-installer, it is easy to install and deploy system services such as
  `docker`, `nvidia-docker`, `nvidia driver`, `ETCD`, `Calico network` etc.
  required by yarn-3.1+.

---

<a id="devdocs-dependencies"></a>

<!-- source_url: https://submarine.apache.org/docs/devDocs/Dependencies/ -->

<!-- page_index: 12 -->

# Dependencies for Submarine

Version: 0.8.0

- These are the dependencies currently used by Apache Submarine.

| Kubernetes Version | Support? |
| --- | --- |
| 1.18.x (or earlier) | X |
| 1.19.x - 1.21.x | Not tested |
| 1.22.x - 1.25.x | √ |
| 1.26.x (or later) | To be verified |

| KinD Version | Support? |
| --- | --- |
| 0.5.x (or earlier) | X |
| 0.6.x - 0.17.x | √ |

| JDK Version | Support? |
| --- | --- |
| 8 | X |
| 11 | √ |
| 17 | To be verified |

- 3.3 or later ( < 3.8.1 )

- Latest

- Version 3

- 14 (or later)

| Go Version | Support? |
| --- | --- |
| 1.15 | X |
| 1.16 | √ |
| 1.17 | √ |
| 1.18 (or later) | X |

| Python Version | Support? |
| --- | --- |
| 3.6 (or earlier) | X |
| 3.7 | √ |
| 3.8 | √ |
| 3.9 | √ |
| 3.10 | √ |

---

<a id="devdocs-buildfromcode"></a>

<!-- source_url: https://submarine.apache.org/docs/devDocs/BuildFromCode/ -->

<!-- page_index: 13 -->

# How to Build Submarine

Version: 0.8.0

- JDK 1.8
- Maven 3.3 or later ( < 3.8.1 )
- Docker

Submarine provides default Docker image in the release artifacts, sometimes you would like to do some modifications on the images. You can rebuild Docker image after you make changes.

> Note that you need to make sure the images built above can be accessed in k8s
> Usually this needs to rename and push to a proper Docker registry.

```bash
mvn clean package -DskipTests 
```

Build submarine server image:

```bash
./dev-support/docker-images/submarine/build.sh 
```

Build submarine database image:

```bash
./dev-support/docker-images/database/build.sh 
```

```text
mvn clean org.apache.rat:apache-rat-plugin:check 
```

- Maven Wrapper (Optional): Maven Wrapper can help you avoid dependencies problem about Maven version.

```text
# Setup Maven Wrapper (Maven 3.6.1) 
mvn -N io.takari:maven:0.7.7:wrapper -Dmaven=3.6.1 
 
# Check Maven Wrapper 
./mvnw -version 
 
# Replace 'mvn' with 'mvnw'. Example: 
./mvnw clean package -DskipTests 
```

---

<a id="devdocs-development"></a>

<!-- source_url: https://submarine.apache.org/docs/devDocs/Development/ -->

<!-- page_index: 14 -->

# Development Guide

Version: 0.8.0

<a id="devdocs-development--project-overview"></a>

# Project Overview

The document [Submarine Quickstart](#gettingstarted-quickstart) shows how to deploy the Submarine service to your Kubernetes cluster. The Submarine service consists mainly of nine components, and you can check them with the following command:

```text
kubectl get pods -n ${your_namespace} 
```

A brief introduction about these components:

1. **tf-operator**: Enable users to run TensorFlow jobs distributedly
2. **pytorch-operator**: Enable users to run PyTorch jobs distributedly
3. **notebook-controller**: Jupyter Notebook controller
4. **submarine-istio**: Kubernetes Ingress controller
5. **submarine-database**: A MySQL database to store metadata
6. **submarine-minio**: An object store for machine learning artifacts
7. **submarine-mlflow**: A platform for model management
8. **submarine-tensorboard**: A visualization tool for distributed training experiments
9. **submarine-server**: Handle API requests, and submit distributed training experiments to Kubernetes.
10. **submarine-agent**: Listening to the status of experiments and notebooks

<a id="devdocs-development--submarine-development"></a>

# Submarine Development

- From this [Video](https://youtu.be/32Na2k6Alv4), you will know how to deal with the configuration of Submarine and be able to contribute to it via Github.

- JDK 11
- Maven 3.3 or later ( < 3.8.1 )
- Docker

Checkstyle plugin may help to detect violations directly from the IDE.

1. Install Checkstyle+IDEA plugin from `Preference` -> `Plugins`
2. Open `Preference` -> `Tools` -> `Checkstyle`
   1. Set Checkstyle version:
      - Checkstyle version: 8.0
   2. Add (+) a new Configuration File
      - Description: Submarine
      - Use a local checkstyle `${SUBMARINE_HOME}/dev-support/maven-config/checkstyle.xml`
3. Open the Checkstyle Tool Window, select the Submarine rule and execute the check

- Unit Test

  For each class, there is a corresponding testClass. For example, `SubmarineServerTest` is used for testing `SubmarineServer`. Whenever you add a funtion in classes, you must write a unit test to test it.
- Integration Test: [IntegrationTestK8s.md](#devdocs-integrationtestk8s)

- Before building

  1. We assume the developer use **minikube** as a local kubernetes cluster.
  2. Make sure you have **installed the submarine helm-chart** in the cluster.

1. Package the Submarine server into a new jar file


```bash
mvn install -DskipTests 
```

2. Build the new server docker image in minikube


```bash
# switch to minikube docker daemon to build image directly in minikube eval $(minikube docker-env)
 
# run docker build./dev-support/docker-images/submarine/build.sh
 
# exit minikube docker daemon eval $(minikube docker-env -u)
```

3. Delete the server deployment and the operator will create a new one using the new image


```bash
kubectl delete deployment submarine-server -n submarine-user-test 
```

1. Deploy the Submarine

   Follow [Getting Started/Quickstart](#gettingstarted-quickstart), and make sure you can connect to `http://localhost:32080` in the browser.
2. Install the dependencies


```bash
cd submarine-workbench/workbench-web 
npm install 
```

3. Run the workbench based on proxy server


```bash
npm run start 
```

   1. The request sent to `http://localhost:4200` will be redirected to `http://localhost:32080`.
   2. Open `http://localhost:4200` in browser to see the real-time change of workbench.
4. Frontend E2E test: [IntegrationTestE2E.md](#devdocs-integrationteste2e)

1. Build the docker image


```bash
# switch to minikube docker daemon to build image directly in minikube eval $(minikube docker-env)
 
# run docker build./dev-support/docker-images/database/build.sh
 
# exit minikube docker daemon eval $(minikube docker-env -u)
```

2. Deploy new pods in the cluster


```bash
helm upgrade --set submarine.database.dev=true submarine ./helm-charts/submarine 
```

For details, please check out the [README](https://github.com/apache/submarine/blob/master/submarine-cloud-v3/README.md) and [Developer Guide](https://github.com/apache/submarine/blob/master/submarine-cloud-v3/docs/developer-guide.md) on GitHub.

Submarine website is built using [Docusaurus 2](https://v2.docusaurus.io/), a modern static website generator.

We store all the website content in markdown format in the `submarine/website/docs`. When committing a new patch to the `submarine` repo, Docusaurus will help us generate the `html` and `javascript` files and push them to <https://github.com/apache/submarine-site/tree/asf-site>.

To update the website, click “Edit this page” on the website.

![](https://lh4.googleusercontent.com/gYcKpxbsGAKv2giTRqkxOehPGnuvnhE31WjsAsYhFmACIZF3Wh2ipar7mZ7F_KRwecM-L1J8YJAgNigJsJUjqc-5IXeO2XGxCIcYpP9CdSc3YByuUkjT_Bezby2HHtkBLyE1ZY_F)

If you want to add a new page to the website, make sure to add the file path to [sidebars.js](https://github.com/apache/submarine/blob/master/website/sidebars.js).

We use the yarn package manager to install all dependencies for the website

```console
yarn install 
```

Make sure you can successfully build the website before creating a pull request.

```console
yarn build 
```

This command starts a local development server and open up a browser window. Most changes are reflected live without having to restart the server.

```console
yarn start 
```

---

<a id="devdocs-integrationtestk8s"></a>

<!-- source_url: https://submarine.apache.org/docs/devDocs/IntegrationTestK8s/ -->

<!-- page_index: 15 -->

# How to Run Integration K8s Test

Version: 0.8.0

- The test cases under the directory `test-k8s` are integration tests to ensure the correctness of the Submarine RESTful API.
- You can run these tests either locally or on GitHub Actions.

  - Before running the tests, the minikube (KinD) cluster must be created.
  - Then, compile and package the submarine project in `submarine-dist` directory for building a docker image.
  - In addition, the 8080 port in submarine-traefik should be forwarded.

1. Ensure you have setup the KinD cluster or minikube cluster. If you haven't, follow this [`minikube tutorial`](https://minikube.sigs.k8s.io/docs/start/)
2. Build the submarine from source and upgrade the server pod through this [`guide`](#devdocs-development--build-from-source)
3. Forward port


```bash
kubectl port-forward --address 0.0.0.0 service/submarine-traefik 8080:80 
```

4. Install the latest package "submarine-server-core" into the local repository, for use as a dependency in the module `test-k8s`


```bash
mvn install -DskipTests 
```

5. Execute the test command


```bash
mvn verify -DskipRat -pl :submarine-test-k8s -Phadoop-2.9 -B 
```

![](assets/images/test-k8s-result-883d99774542cc9898f086937cb80190_f1223ef5852737bc.png)

- Each time a code is submitted, GitHub Actions is triggered automatically.

---

<a id="devdocs-integrationteste2e"></a>

<!-- source_url: https://submarine.apache.org/docs/devDocs/IntegrationTestE2E/ -->

<!-- page_index: 16 -->

# How to Run Frontend Integration Test

Version: 0.8.0

- The test cases under the directory [test-e2e](https://github.com/apache/submarine/tree/master/submarine-test/test-e2e/src/test/java/org/apache/submarine/integration) are integration tests to ensure the correctness of the Submarine Workbench.
- These test cases can be run either locally or on GitHub Actions.

1. Ensure you have setup the submarine locally. If not, you can refer to [Quickstart](#gettingstarted-quickstart).
2. Forward port


```bash
kubectl port-forward --address 0.0.0.0 service/submarine-traefik 32080:80 
```

3. Modify run\_frontend\_e2e.sh

   You need to modify the port and the URL in this script to where you run the workbench on.

   > Example:
   > If your Submarine workbench is running on 127.0.0.1:4200, you should modify the **WORKBENCH\_PORT** to 4200.


```bash
# at submarine-test/test_e2e/run_frontend_e2e.sh ...# ======= Modifiable Variables ======= # # Note: URL must start with "http" # (Ref: https://www.selenium.dev/selenium/docs/api/java/org/openqa/selenium/WebDriver.html#get(java.lang.String)) WORKBENCH_PORT=8080 #<= modify this URL="http://127.0.0.1" #<=modify this # ==================================== # ...
```

4. Run `run_frontend_e2e.sh` (Run a specific test case)

   This script will check whether the port can be accessed or not, and run the test case.


```bash
# at submarine-test/test_e2e./run_fronted_e2e.sh ${TESTCASE}
# TESTCASE is the IT you want to run, ex: loginIT, experimentIT...
```

5. Run all test cases

- Following commands will compile all files and run all files ending with "IT" in the [directory](https://github.com/apache/submarine/tree/master/submarine-test/test-e2e/src/test/java/org/apache/submarine/integration).


```bash
# Make sure the Submarine workbench is running on 127.0.0.1:8080 cd submarine/submarine-test/test-e2e
# Method 1:mvn verify
 
# Method 2:mvn clean install -U
```

- Each time a commit is pushed, GitHub Actions will be triggered automatically.

> [!WARNING]
> - - You **MUST** read the [document](https://www.selenium.dev/documentation/en/webdriver/waits/) carefully, and understand the difference between **explicit wait**, **implicit wait**, and **fluent wait**.
>   - **Do not mix implicit and explicit waits.** Doing so can cause unpredictable wait times.
- We define many useful functions in [AbstractSubmarineIT.java](https://github.com/apache/submarine/blob/master/submarine-test/test-e2e/src/test/java/org/apache/submarine/AbstractSubmarineIT.java).

---

<a id="devdocs-howtorelease"></a>

<!-- source_url: https://submarine.apache.org/docs/devDocs/HowToRelease/ -->

<!-- page_index: 17 -->

# How to Release

Version: 0.8.0

> This article mainly introduces how the Release Manager releases a specific version of the project according to the Apache process.

Source Release is the focus of Apache’s attention and it is also a required content for release. Binary Release is optional, Submarine can choose whether to release the binary package to the Apache warehouse or to the Maven central warehouse.

Please refer to the following link to find more details about release guidelines:

[How to Release](https://cwiki.apache.org/confluence/display/SUBMARINE/How+to+release)
[Submarine Release Guidelines](https://cwiki.apache.org/confluence/display/SUBMARINE/Submarine+Release+Guidelines)

> Main references in this chapter:<https://infra.apache.org/openpgp.html> > **This chapter is only needed for the first release manager of the project.**

Detailed installation documents can refer to [tutorial](https://www.gnupg.org/download/index.html), The environment configuration of Mac OS is as follows:

```shell
$ brew install gpg
$ gpg --version #Check the version，should be 2.x
```

- When entering the name, it is better to be consistent with the Full name registered in Apache
- The mailbox used should be apache mailbox
- It’s better to use pinyin or English for the name, otherwise there will be garbled characters

```shell
➜  ~ gpg --full-gen-key 
gpg (GnuPG) 2.2.20; Copyright (C) 2020 Free Software Foundation, Inc. 
This is free software: you are free to change and redistribute it. 
There is NO WARRANTY, to the extent permitted by law. 
 
Please select what kind of key you want: 
   (1) RSA and RSA (default) 
   (2) DSA and Elgamal 
   (3) DSA (sign only) 
   (4) RSA (sign only) 
  (14) Existing key from card 
Your selection? 1 # enter 1 here 
RSA keys may be between 1024 and 4096 bits long. 
What keysize do you want? (2048) 4096 # enter 4096 here 
Requested keysize is 4096 bits 
Please specify how long the key should be valid. 
         0 = key does not expire 
      <n>  = key expires in n days 
      <n>w = key expires in n weeks 
      <n>m = key expires in n months 
      <n>y = key expires in n years 
Key is valid for? (0) 0 # enter 0 here 
Key does not expire at all 
Is this correct? (y/N) y # enter y here 
 
GnuPG needs to construct a user ID to identify your key. 
 
Real name: Guangxu Cheng # enter your name here 
Email address: gxcheng@apache.org # enter your mailbox here 
Comment:                          # enter some comment here (Optional) 
You selected this USER-ID: 
    "Guangxu Cheng <gxcheng@apache.org>" 
 
Change (N)ame, (C)omment, (E)mail or (O)kay/(Q)uit? O #enter O here 
We need to generate a lot of random bytes. It is a good idea to perform 
some other action (type on the keyboard, move the mouse, utilize the 
disks) during the prime generation; this gives the random number 
generator a better chance to gain enough entropy. 
We need to generate a lot of random bytes. It is a good idea to perform 
some other action (type on the keyboard, move the mouse, utilize the 
disks) during the prime generation; this gives the random number 
generator a better chance to gain enough entropy. 
 
# A dialog box will pop up, asking you to enter the key for this gpg. ┌──────────────────────────────────────────────────────┐ │ Please enter this passphrase │ │ │ │ Passphrase: _______________________________ │ │ │ │ <OK> <Cancel> │ └──────────────────────────────────────────────────────┘
# After entering the secret key, it will be created. And it will output the following information. gpg: key 2DD587E7B10F3B1F marked as ultimately trusted gpg: revocation certificate stored as '/Users/cheng/.gnupg/openpgp-revocs.d/41936314E25F402D5F7D73152DD587E7B10F3B1F.rev' public and secret key created and signed.
 
pub   rsa4096 2020-05-19 [SC] 
      41936314E25F402D5F7D73152DD587E7B10F3B1F 
uid                      Guangxu Cheng <gxcheng@apache.org> 
sub   rsa4096 2020-05-19 [E] 
```

```shell
➜  ~ gpg --list-keys 
------------------------------- 
pub   rsa4096 2020-05-18 [SC] 
      5931F8CFD04B37A325E4465D8C0D31C4149B3A87 
uid           [ultimate] Guangxu Cheng <gxcheng@apache.org> 
sub   rsa4096 2020-05-18 [E] 
 
# Send public key to keyserver via key id
$ gpg --keyserver pgpkeys.mit.edu --send-key <key id>
# Among them, pgpkeys.mit.edu is a randomly selected keyserver, and the keyserver list is: https://sks-keyservers.net/status/, which is automatically synchronized with each other, you can choose any one.
```

Through the following URL, use the email to check whether the upload is successful or not. It will take about a minute to find out. When searching, check the show full-key hashes under advance on <http://pgpkeys.mit.edu> .

The query results are as follows:

> SVN is required for this step

The svn library of the DEV branch is <https://dist.apache.org/repos/dist/dev/submarine>

The SVN library of the Release branch is <https://dist.apache.org/repos/dist/release/submarine>

```shell
➜  ~ svn co https://dist.apache.org/repos/dist/dev/submarine /tmp/submarine-dist-dev 
# This step is relatively slow, and all versions will be copied. If the network is disconnected, use svn cleanup to delete the lock and re-execute it, and the transfer will be resumed. ➜ ~ cd submarine-dist-dev ➜ submarine-dist-dev ~ (gpg --list-sigs YOUR_NAME@apache.org && gpg --export --armor YOUR_NAME@apache.org) >> KEYS # Append the KEY you generated to the file KEYS, it is best to check if it is correct after appending. ➜ submarine-dist-dev ~ svn add . # If there is a KEYS file before, it is not needed. ➜ submarine-dist-dev ~ svn ci -m "add gpg key for YOUR_NAME" # Next, you will be asked to enter a username and password, just use your apache username and password.
```

```shell
➜  ~ svn co https://dist.apache.org/repos/dist/release/submarine /tmp/submarine-dist-release 
➜  ~ cd submarine-dist-release 
➜  submarine-dist-release ~ (gpg --list-sigs YOUR_NAME@apache.org && gpg --export --armor YOUR_NAME@apache.org) >> KEYS # Append the KEY you generated to the file KEYS, it is best to check if it is correct after appending. 
➜  submarine-dist-release ~ svn add .   # If there is a KEYS file before, it is not needed. 
➜  submarine-dist-release ~ svn ci -m "add gpg key for YOUR_NAME" # Next, you will be asked to enter a username and password, just use your apache username and password. 
```

1. Go to <https://github.com/settings/keys> and add GPG KEYS.
2. If you find "unverified" is written after the key after adding it, remember to bind the mailbox used in the GPG key to your github account (<https://github.com/settings/emails>).

**Skip if it has already been set**

In the maven configuration file ~/.m2/settings.xml, add the following `<server>` item

```xml
<?xml version="1.0" encoding="UTF-8"?> 
<settings xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.1.0 http://maven.apache.org/xsd/settings-1.1.0.xsd" xmlns="http://maven.apache.org/SETTINGS/1.1.0" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"> 
  <servers> 
    <!-- Apache Repo Settings --> 
    <server> 
        <id>apache.snapshots.https</id> 
        <username>{user-id}</username> 
        <password>{user-pass}</password> 
    </server> 
    <server> 
        <id>apache.releases.https</id> 
        <username>{user-id}</username> 
        <password>{user-pass}</password> 
    </server> 
  </servers> 
<profiles> 
    <profile> 
      <id>apache-release</id> 
      <properties> 
        <gpg.keyname>Your KEYID</gpg.keyname><!-- Your GPG Keyname here --> 
        <!-- Use an agent: Prevents being asked for the password during the build --> 
        <gpg.useagent>true</gpg.useagent> 
        <gpg.passphrase>Your password of the private key</gpg.passphrase> 
      </properties> 
    </profile> 
</profiles> 
</settings> 
```

- Pull the new branch from the main branch as a release branch, release-${release\_version}
- Update `CHANGES.md`
- Check whether the code is normal, including successful compilation, all unit tests, successful RAT check, etc.


```shell
# build check
$ mvn clean package -Dmaven.javadoc.skip=true
# RAT check
$ mvn apache-rat:check
```

- Change the version number

> Before creating the tag, make sure that the code has been checked for errors, including: successful compilation, all unit tests, and successful RAT checks, etc.

**Create a tag with signature**

```shell
$ git_tag=${release_version}-${rc_version}
$ git tag -s $git_tag -m "Tagging the ${release_version} first Releae Candidate (Candidates start at zero)"
# If a error happened like gpg: signing failed: secret key not available, set the private key first.
$ git config user.signingkey ${KEY_ID}
```

> After the tag is successfully created, the tag source code should be packaged into a tar package.

```shell
mkdir /tmp/apache-submarine-${release_version}-${rc_version} 
git archive --format=tar.gz --output="/tmp/apache-submarine-${release_version}-${rc_version}/apache-submarine-${release_version}-src.tar.gz" --prefix="apache-submarine-${release_version}/" $git_tag 
```

> Compile the source code packaged in the previous step

```shell
cd /tmp/apache-submarine-${release_version}-${rc_version} # Enter the source package directory. 
tar xzvf apache-submarine-${release_version}-src.tar.gz # Unzip the source package. 
cd apache-submarine-${release_version} # Enter the source directory. 
mvn compile clean install package -DskipTests # Compile. 
cp ./submarine-distribution/target/apache-submarine-${release_version}-bin.tar.gz /tmp/apache-submarine-${release_version}-${rc_version}/  # Copy the binary package to the source package directory to facilitate signing the package in the next step. 
```

```shell
for i in *.tar.gz; do echo $i; gpg --print-md SHA512 $i > $i.sha512 ; done # Calculate SHA512 
for i in *.tar.gz; do echo $i; gpg --armor --output $i.asc --detach-sig $i ; done # Calculate the signature 
```

For example, verify that the signature is correct as follows:

```shell
for i in *.tar.gz; do echo $i; gpg --verify $i.asc $i ; done 
```

```shell
cd /tmp/apache-submarine-${release_version}-${rc_version} # Enter the source package directory 
tar xzvf apache-submarine-${release_version}-src.tar.gz # Unzip the source package 
cd apache-submarine-${release_version} 
mvn -DskipTests deploy -Papache-release -Dmaven.javadoc.skip=true  # Start upload 
```

```shell
git push origin ${release_version}-${rc_version} 
```

> This step requires the use of SVN, the svn library of the DEV branch is <https://dist.apache.org/repos/dist/dev/submarine>

```shell
# This step may be slow, and all versions will be tested. If the network is broken, use svn cleanup to delete the lock and re-execute it, and the upload will be resumed. svn co https://dist.apache.org/repos/dist/dev/submarine /tmp/submarine-dist-dev
```

```shell
cd /tmp/submarine-dist-dev 
mkdir ${release_version}-${rc_version} # Create version directory 
# Copy the source code package and signed package here. cp /tmp/apache-submarine-${release_version}-${rc_version}/*tar.gz* ${release_version}-${rc_version}/svn status # Check svn status. svn add ${release_version}-${rc_version} # Add to svn version. svn status # Check svn status. svn commit -m "prepare for ${release_version} ${rc_version}" # Submit to svn remote server.
```

> Please make sure all artifacts are fine.

1. **Log in** <http://repository.apache.org> , with Apache account
2. Click on Staging repositories on the left.
3. Search for Submarine keywords and select the repository you uploaded recently.
4. Click the Close button above, and a series of checks will be performed during this process.
5. After the check is passed, a link will appear on the Summary tab below. Please save this link and put it in the next voting email.
   The link should look like: `https://repository.apache.org/content/repositories/orgapachesubmarine-xxxx`

WARN: Please note that clicking Close may fail, please check the reason for the failure and deal with it.

> To vote in the Submarine community, send an email to:`dev@submarine.apache.org`

```text
Title：[VOTE] Submarine-${release_version}-${rc_version} is ready for a vote! 
 
Content： 
 
Hi folks, 
 
Thanks to everyone's help on this release. 
 
I've created a release candidate (${rc_version}) for submarine ${release_version}. The 
highlighted features are as follows: 
 
1. AAA 
2. BBB 
3. CCC 
 
The mini-submarine image is here: 
 
docker pull apache/submarine:mini-${release_version}-${rc_version} 
 
 
The RC tag in git is here: 
 
https://github.com/apache/submarine/releases/tag/release-${release_version}-${rc_version} 
 
The RC release artifacts are available at: 
 
http://home.apache.org/~pingsutw/submarine-${release_version}-${rc_version} 
 
 
The Maven staging repository is here: 
 
https://repository.apache.org/content/repositories/orgapachesubmarine-1030 
 
My public key is here: 
 
https://dist.apache.org/repos/dist/release/submarine/KEYS 
 
 
*This vote will run for 7 days, ending on DDDD/EE/FF at 11:59 pm PST.* 
 
 
For the testing, I have verified the 
 
1. Build from source, Install Submarine on minikube 
 
2. Workbench UI (Experiment / Notebook / Template / Environment) 
 
3. Experiment / Notebook / Template / Environment REST API 
 
 
My +1 to start. Thanks! 
 
BR, 
XXX 
 
```

```text
Title：[RESULT][VOTE] Release Apache Submarine ${release_version} ${rc_version} 
 
Content： 
 
Hello Apache Submarine PMC and Community, 
  The vote closes now as 72hr have passed. The vote PASSES with 
  xx (+1 non-binding) votes from the PMC, 
  xx (+1 non-binding) vote from the rest of the developer community, 
  and no further 0 or -1 votes. 
 
  The vote thread:{vote_mail_address} 
 
Thank you for your support. 
Your Submarine Release Manager 
```

> Please make sure all artifacts are fine.

1. Log in to <http://repository.apache.org> with your Apache account.
2. Click on Staging repositories on the left.
3. Search for Submarine keywords, select your recently uploaded repository, the repository specified in the voting email.
4. Click the `Release` button above, and a series of checks will be carried out during this process.
   **It usually takes 24 hours to wait for the repository to synchronize to other data sources**

**Please make sure that the repository in 6.4 has been successfully released, generally the email is sent 24 hours after 6.4**

Announce release email template:

```text
Title： [ANNOUNCE] Apache Submarine ${release_version} release! 
Content： 
Hi folks, It's a great honor for me to announce that the Apache Submarine Community 
has released Apache Submarine ${release_version}! 
The highlighted features are: 
1. AAA 
2. BBB 
3. CCC 
 
Tons of thanks to our contributors and community! 
Let's keep fighting! *Apache Submarine ${release_version} released*: 
https://submarine.apache.org/docs/next/releases/submarine-release-${release_version} 
 
BR, 
XXXX 
```

---

<a id="devdocs-howtoverify"></a>

<!-- source_url: https://submarine.apache.org/docs/devDocs/HowToVerify/ -->

<!-- page_index: 18 -->

# How to Verify

Version: 0.8.0

```shell
svn co https://dist.apache.org/repos/dist/dev/submarine/${release_version}-${rc_version}/ 
```

> Begin the verification process, which includes but is not limited to the following content and forms.

> The package uploaded to dist must include the source code package, and the binary package is optional.

1. Whether it includes the source code package.
2. Whether it includes the signature of the source code package.
3. Whether it includes the sha512 of the source code package.
4. If the binary package is uploaded, also check the contents listed in (2)-(4).

- Import the public key

```shell
curl https://dist.apache.org/repos/dist/dev/submarine/KEYS > KEYS # Download KEYS 
gpg --import KEYS # Import KEYS to local 
```

- Trust the public key
  > Trust the KEY used in this version.

```text
  gpg --edit-key xxxxxxxxxx # The KEY used in this version 
  gpg (GnuPG) 2.2.21; Copyright (C) 2020 Free Software Foundation, Inc. 
  This is free software: you are free to change and redistribute it. 
  There is NO WARRANTY, to the extent permitted by law. 
 
  Secret key is available. 
 
  sec  rsa4096/5EF3A66D57EC647A 
       created: 2020-05-19  expires: never       usage: SC 
       trust: ultimate      validity: ultimate 
  ssb  rsa4096/17628566FEED6AF7 
       created: 2020-05-19  expires: never       usage: E 
  [ultimate] (1). XXX YYYZZZ <yourAccount@apache.org> 
 
  gpg> trust 
  sec  rsa4096/5EF3A66D57EC647A 
       created: 2020-05-19  expires: never       usage: SC 
       trust: ultimate      validity: ultimate 
  ssb  rsa4096/17628566FEED6AF7 
       created: 2020-05-19  expires: never       usage: E 
  [ultimate] (1). XXX YYYZZZ <yourAccount@apache.org> 
 
  Please decide how far you trust this user to correctly verify other users' keys 
  (by looking at passports, checking fingerprints from different sources, etc.) 
 
    1 = I don't know or won't say 
    2 = I do NOT trust 
    3 = I trust marginally 
    4 = I trust fully 
    5 = I trust ultimately 
    m = back to the main menu 
 
  Your decision? 5 #choose 5 
  Do you really want to set this key to ultimate trust? (y/N) y # choose y 
 
  sec  rsa4096/5EF3A66D57EC647A 
       created: 2020-05-19  expires: never       usage: SC 
       trust: ultimate      validity: ultimate 
  ssb  rsa4096/17628566FEED6AF7 
       created: 2020-05-19  expires: never       usage: E 
  [ultimate] (1). XXX YYYZZZ <yourAccount@apache.org> 
 
  gpg> 
 
  sec  rsa4096/5EF3A66D57EC647A 
       created: 2020-05-19  expires: never       usage: SC 
       trust: ultimate      validity: ultimate 
  ssb  rsa4096/17628566FEED6AF7 
       created: 2020-05-19  expires: never       usage: E 
  [ultimate] (1). XXX YYYZZZ <yourAccount@apache.org> 
```

- Use the following command to check the signature.

```shell
for i in *.tar.gz; do echo $i; gpg --verify $i.asc $i ; done 
#Or 
gpg --verify apache-submarine-${release_version}-src.tar.gz.asc apache-submarine-${release_version}-src.tar.gz 
# If you upload a binary package, you also need to check whether the signature of the binary package is correct. gpg --verify apache-submarine-server-${release_version}-bin.tar.gz.asc apache-submarine-server-${release_version}-bin.tar.gz gpg --verify apache-submarine-client-${release_version}-bin.tar.gz.asc apache-submarine-client-${release_version}-bin.tar.gz
```

- Check the result
  > If something like the following appears, it means that the signature is correct. The keyword：**`Good signature`**

```shell
apache-submarine-${release_version}-src.tar.gz 
gpg: Signature made Sat May 30 11:45:01 2020 CST 
gpg:                using RSA key 9B12C2228BDFF4F4CFE849445EF3A66D57EC647A 
gpg: Good signature from "XXX YYYZZZ <yourAccount@apache.org>" [ultimate]gular2 
```

> After calculating the sha512 hash locally, verify whether it is consistent with the one on dist.

```shell
for i in *.tar.gz; do echo $i; gpg --print-md SHA512 $i; done 
#Or 
gpg --print-md SHA512 apache-submarine-${release_version}-src.tar.gz 
# If you upload a binary package, you also need to check the sha512 hash of the binary package. gpg --print-md SHA512 apache-submarine-server-${release_version}-bin.tar.gz gpg --print-md SHA512 apache-submarine-client-${release_version}-bin.tar.gz
# 或者 for i in *.tar.gz.sha512; do echo $i; sha512sum -c $i; done
```

Unzip `apache-submarine-${release_version}-src.tar.gz` and check as follows:

- Whether the DISCLAIMER file exists and whether the content is correct.
- Whether the LICENSE and NOTICE file exists and whether the content is correct.
- Whether all files have ASF License header.
- Whether the source code can be compiled normally.
- Whether the single test is passed.
- ....

Unzip `apache-submarine-client-${release_version}-src.tar.gz` and  `apache-submarine-server-${release_version}-src.tar.gz`, then check as follows:

- Whether the DISCLAIMER file exists and whether the content is correct.
- Whether the LICENSE and the NOTICE file exists and whether the content is correct.
- Whether the deployment is successful.
- Deploy a test environment to verify whether production and consumption can run normally.
- Verify what you think might go wrong.

---

<a id="community"></a>

<!-- source_url: https://submarine.apache.org/docs/community/ -->

<!-- page_index: 19 -->

# Apache Submarine Community

Version: 0.8.0

Welcome to the Apache Submarine Community! The main objective is to help members of the Submarine community who share similar interests to learn from and collaborate with each other.

Your journey of becoming a contributor and committer starts from here: improving docs, improving code, giving talks, organizing meetups, etc.

You can reach out to the community members via any one of the following ways:

- Slack Developer: [https://join.slack.com/t/asf-submarine/shared\_invite](https://join.slack.com/t/asf-submarine/shared_invite/zt-18614cyqs-UhspdUOneiyg~ZPiVomDqw)


> [!NOTE]
> **<a id="community--info"></a>

 info**
> After clicking the link above, you would join the ASF Submarine channel.

- Zoom: <https://cloudera.zoom.us/j/97264903288>
- Sync Up: <https://docs.google.com/document/d/16pUO3TP4SxSeLduG817GhVAjtiph9HYpRHo_JgduDvw/edit>

You can start by finding an existing issue with the <https://issues.apache.org/jira/projects/SUBMARINE/issues/SUBMARINE?filter=allopenissues> label. These issues are well suited for new contributors.

If a PR (Pull Request) submitted to the [Submarine Github](https://github.com/apache/submarine) projects by you is approved and merged, then you become a Submarine Contributor.

If you want to work on a new idea of relatively small scope:

1. Submit an issue describing your proposed change to the repo in question.
2. The repo owners will respond to your issue promptly.
3. Submit a [pull request of Submarine](https://github.com/apache/submarine) containing a tested change.

Contributions are welcomed and greatly appreciated. See [CONTRIBUTING](#community-contributing) for details on submitting patches and the contribution workflow.

First of all, you need to get involved and be a Contributor.

Based on your track-record as a contributor, Per Apache code, PMCs vote on committership, may invite you to be a committer (after we've called a vote). When that happens, if you accept, the following process kicks into place...

Note that becoming a committer is not just about submitting some patches; it‘s also about helping out on the development and user, helping with documentation and the issues.

See [How to become an Apache Submarine Committer and PMC](#community-howtobecomecommitter) for more details.

See [How to commit](#community-howtocommit) for helper doc for Submarine committers.

Communication within the Submarine community abides by [Apache’s Code of Conduct](https://www.apache.org/foundation/policies/conduct.html).

Get help using Apache Submarine or contribute to the project on our mailing lists:

- [Users](https://lists.apache.org/list.html?users@submarine.apache.org) : [subscribe](mailto:users-subscribe@submarine.apache.org), [unsubscribe](mailto:users-unsubscribe@submarine.apache.org), [archives](https://lists.apache.org/list.html?users@submarine.apache.org)
  for usage questions, help, and announcements.
- [Dev](https://lists.apache.org/list.html?dev@submarine.apache.org) : [subscribe](mailto:dev-subscribe@submarine.apache.org), [unsubscribe](mailto:dev-unsubscribe@submarine.apache.org), [archives](https://lists.apache.org/list.html?dev@submarine.apache.org)
  for people wanting to contribute to the project.
- [Commits](https://lists.apache.org/list.html?commits@submarine.apache.org) : [subscribe](mailto:commits-subscribe@submarine.apache.org), [unsubscribe](mailto:commits-unsubscribe@submarine.apache.org), [archives](https://lists.apache.org/list.html?commits@submarine.apache.org)
  for commit messages and patches.

Take subscribe Dev as an example, you should send an email to [dev-subscribe@submarine.apache.org](mailto:dev-subscribe@submarine.apache.org).

Usually, this happens when you just click the "subscribe" link. If this does not work, simply copy the address and paste it into the "To:" field of a new message.

After that, you will get an email from [dev-help@submarine.apache.org](mailto:dev-help@submarine.apache.org), follow the directives of the mail to reply, then you will subscribe [dev@submarine.apache.org](mailto:dev@submarine.apache.org) successfully.

Submarine source code is under the Apache 2.0 license. See the [LICENSE](https://github.com/apache/submarine/blob/master/LICENSE) file for details.

---

<a id="community-bylaws"></a>

<!-- source_url: https://submarine.apache.org/docs/community/Bylaws/ -->

<!-- page_index: 20 -->

# Bylaws

Version: 0.8.0

This document defines the bylaws under which the Apache Submarine project operates. It defines the roles and responsibilities of the project, who may vote, how voting works, how conflicts are resolved, etc.

Submarine is a project of the [Apache Software Foundation](https://www.apache.org/foundation/). The foundation holds the trademark on the name “Submarine” and copyright on Apache code including the code in the Submarine codebase. The [foundation FAQ](https://www.apache.org/foundation/faq.html) explains the operation and background of the foundation.

Submarine is typical of Apache projects in that it operates under a set of principles, known collectively as the “Apache Way”. If you are new to Apache development, please refer to the [Incubator project](http://incubator.apache.org) for more information on how Apache projects operate.

<a id="community-bylaws--roles-and-responsibilities"></a>

# Roles and Responsibilities

Apache projects define a set of roles with associated rights and responsibilities. These roles govern what tasks an individual may perform within the project. The roles are defined in the following sections

- **Users**

  The most important participants in the project are people who use our software. The majority of our developers start out as users and guide their development efforts from the user’s perspective.

  Users contribute to the Apache projects by providing feedback to developers in the form of bug reports and feature suggestions. As well, users participate in the Apache community by helping other users on mailing lists and user support forums.
- **Contributors**

  All of the volunteers who are contributing time, code, documentation, or resources to the Submarine Project. A contributor that makes sustained, welcome contributions to the project may be invited to become a Committer, though the exact timing of such invitations depends on many factors.
- **Committers**

  The project’s Committers are responsible for the project’s technical management. Committers have access to all subproject subversion repositories. Committers may cast binding votes on any technical discussion regarding any subproject.

  Committer access is by invitation only and must be approved by consensus approval of the active PMC members. A Committer is considered emeritus by their own declaration or by not contributing in any form to the project for over six months. An emeritus committer may request reinstatement of commit access from the PMC. Such reinstatement is subject to consensus approval of active PMC members.

  Significant, pervasive features are often developed in a speculative branch of the repository. The PMC may grant commit rights on the branch to its consistent contributors, while the initiative is active. Branch committers are responsible for shepherding their feature into an active release and do not cast binding votes or vetoes in the project.

  All Apache committers are required to have a signed Contributor License Agreement (CLA) on file with the Apache Software Foundation. There is a [Committer FAQ](https://www.apache.org/dev/committers.html) which provides more details on the requirements for Committers

  A committer who makes a sustained contribution to the project may be invited to become a member of the PMC. The form of contribution is not limited to code. It can also include code review, helping out users on the mailing lists, documentation, testing, etc.
- **Release Manager**

  A Release Manager (RM) is a committer who volunteers to produce a Release Candidate according to [HowToRelease](https://github.com/apache/submarine/blob/master/dev-support/cicd/HowToRelease.md). The RM shall publish a Release Plan on the *common-dev@* list stating the branch from which they intend to make a Release Candidate, at least one week before they do so. The RM is responsible for building consensus around the content of the Release Candidate, in order to achieve a successful Product Release vote.
- **Project Management Committee**

  The Project Management Committee (PMC) for Apache Submarine was created by the Apache Board in October 2019 when Submarine moved out of Hadoop and became a top level project at Apache. The PMC is responsible to the board and the ASF for the management and oversight of the Apache Submarine codebase. The responsibilities of the PMC include

  - Deciding what is distributed as products of the Apache Submarine project. In particular all releases must be approved by the PMC
  - Maintaining the project’s shared resources, including the codebase repository, mailing lists, websites.
  - Speaking on behalf of the project.
  - Resolving license disputes regarding products of the project
  - Nominating new PMC members and committers
  - Maintaining these bylaws and other guidelines of the project

  Membership of the PMC is by invitation only and must be approved by a consensus approval of active PMC members. A PMC member is considered “emeritus” by their own declaration or by not contributing in any form to the project for over six months. An emeritus member may request reinstatement to the PMC. Such reinstatement is subject to consensus approval of the active PMC members.

  The chair of the PMC is appointed by the ASF board. The chair is an office holder of the Apache Software Foundation (Vice President, Apache Submarine) and has primary responsibility to the board for the management of the projects within the scope of the Submarine PMC. The chair reports to the board quarterly on developments within the Submarine project.

  The chair of the PMC is rotated annually. When the chair is rotated or if the current chair of the PMC resigns, the PMC votes to recommend a new chair using Single Transferable Vote (STV) voting. See <https://wiki.apache.org/general/BoardVoting> for specifics. The decision must be ratified by the Apache board.

<a id="community-bylaws--decision-making"></a>

# Decision Making

Within the Submarine project, different types of decisions require different forms of approval. For example, the previous section describes several decisions which require “consensus approval” approval. This section defines how voting is performed, the types of approvals, and which types of decision require which type of approval.

- **Voting**

  Decisions regarding the project are made by votes on the primary project development mailing list ([dev@submarine.apache.org](mailto:dev@submarine.apache.org)). Where necessary, PMC voting may take place on the private Submarine PMC mailing list. Votes are clearly indicated by subject line starting with [VOTE]. Votes may contain multiple items for approval and these should be clearly separated. Voting is carried out by replying to the vote mail. Voting may take four flavors

  - **+1** “Yes,” “Agree,” or “the action should be performed.” In general, this vote also indicates a willingness on the behalf of the voter in “making it happen”
  - **+0** This vote indicates a willingness for the action under consideration to go ahead. The voter, however will not be able to help.
  - **-0** This vote indicates that the voter does not, in general, agree with the proposed action but is not concerned enough to prevent the action going ahead.
  - **-1** This is a negative vote. On issues where consensus is required, this vote counts as a **veto**. All vetoes must contain an explanation of why the veto is appropriate. Vetoes with no explanation are void. It may also be appropriate for a -1 vote to include an alternative course of action.

  All participants in the Submarine project are encouraged to show their agreement with or against a particular action by voting. For technical decisions, only the votes of active committers are binding. Non binding votes are still useful for those with binding votes to understand the perception of an action in the wider Submarine community. For PMC decisions, only the votes of PMC members are binding.

  Voting can also be applied to changes made to the Submarine codebase. These typically take the form of a veto (-1) in reply to the commit message sent when the commit is made.
- **Approvals**

  These are the types of approvals that can be sought. Different actions require different types of approvals

  - **Consensus Approval -** Consensus approval requires 3 binding +1 votes and no binding vetoes.
  - **Lazy Consensus -** Lazy consensus requires no -1 votes (‘silence gives assent’).
  - **Lazy Majority -** A lazy majority vote requires 3 binding +1 votes and more binding +1 votes than -1 votes.
  - **Lazy 2⁄3 Majority -** Lazy 2⁄3 majority votes requires at least 3 votes and twice as many +1 votes as -1 votes.
- **Vetoes**

  A valid, binding veto cannot be overruled. If a veto is cast, it must be accompanied by a valid reason explaining the reasons for the veto. The validity of a veto, if challenged, can be confirmed by anyone who has a binding vote. This does not necessarily signify agreement with the veto - merely that the veto is valid.

  If you disagree with a valid veto, you must lobby the person casting the veto to withdraw their veto. If a veto is not withdrawn, any action that has been vetoed must be reversed in a timely manner.
- **Actions**

  This section describes the various actions which are undertaken within the project, the corresponding approval required for that action and those who have binding votes over the action.

  - **Code Change**

    A change made to a codebase of the project and committed by a committer. This includes source code, documentation, website content, etc.

    Consensus approval of active committers, but with a minimum of one +1. The code can be committed after the first +1, unless the code change represents a merge from a branch, in which case three +1s are required.
  - **Product Release**

    When a release of one of the project’s products is ready, a vote is required to accept the release as an official release of the project.

    Lazy Majority of active PMC members
  - **Adoption of New Codebase**

    When the codebase for an existing, released product is to be replaced with an alternative codebase. If such a vote fails to gain approval, the existing code base will continue.

    This also covers the creation of new sub-projects within the project

    Lazy 2⁄3 majority of PMC members
  - **New Branch Committer**

    When a branch committer is proposed for the PMC

    Lazy consensus of active PMC members
  - **New Committer**

    When a new committer is proposed for the project

    Consensus approval of active PMC members
  - **New PMC Member**

    When a committer is proposed for the PMC

    Consensus approval of active PMC members
  - **Branch Committer Removal**

    When removal of commit privileges is sought **or** when the branch is merged to the mainline

    Lazy 2⁄3 majority of active PMC members
  - **Committer Removal**

    When removal of commit privileges is sought. Note: Such actions will also be referred to the ASF board by the PMC chair

    Lazy 2⁄3 majority of active PMC members (excluding the committer in question if a member of the PMC).
  - **PMC Member Removal**

    When removal of a PMC member is sought. Note: Such actions will also be referred to the ASF board by the PMC chair.

    Lazy 2⁄3 majority of active PMC members (excluding the member in question)
  - **Modifying Bylaws**

    Modifying this document.

    Lazy majority of active PMC members
- **Voting Timeframes**

  Votes are open for a period of 7 days to allow all active voters time to consider the vote. Votes relating to code changes are not subject to a strict timetable but should be made as timely as possible.

  - **Product Release - Vote Timeframe**

    Release votes, alone, run for a period of 5 days. All other votes are subject to the above timeframe of 7 days.

---

<a id="community-howtocommit"></a>

<!-- source_url: https://submarine.apache.org/docs/community/HowToCommit/ -->

<!-- page_index: 21 -->

# Guide for Apache Submarine Committers

Version: 0.8.0

This page contains Hadoop Core-specific guidelines for committers.

New committers are encouraged to first read Apache's generic committer documentation:

- [Apache New Committer Guide](http://www.apache.org/dev/new-committers-guide.html)
- [Apache Committer FAQ](http://www.apache.org/dev/committers.html)

The first act of a new core committer is typically to add their name to the
credits page. This requires changing the site source in
<https://github.com/apache/submarine-site/blob/master/community/member.md>. Once done, update the Submarine website as described
[here](https://github.com/apache/submarine-site/blob/asf-site/README.md)
(TLDR; don't forget to regenerate the site with hugo, and commit the generated
results, too).

Submarine committers should, as often as possible, attempt to review patches
submitted by others. Ideally every submitted patch will get reviewed by a
committer within a few days. If a committer reviews a patch they've not
authored, and believe it to be of sufficient quality, then they can commit the
patch, otherwise the patch should be cancelled with a clear explanation for why
it was rejected.

The list of submitted patches can be found in the GitHub
[Pull Requests](https://github.com/apache/submarine/pulls) page.
Committers should scan the list from top-to-bottom, looking for patches that they feel qualified to review and possibly commit.

For non-trivial changes, it is best to get another committer to review & approve
your own patches before commit.

Patches should be rejected which do not adhere to the guidelines in
[Contribution Guidelines](#community-contributing). Committers should always be
polite to contributors and try to instruct and encourage them to contribute
better patches. If a committer wishes to improve an unacceptable patch, then it
should first be rejected, and a new patch should be attached by the committer
for review.

Submarine uses git for source code version control. The writable repo is at -
<https://gitbox.apache.org/repos/asf/submarine.git>

It is strongly recommended to use the cicd script to merge the PRs.
See the instructions at
<https://github.com/apache/submarine/tree/master/dev-support/cicd>

There are three roles (Administrators, Committers, Contributors) in the project.

- Contributors who have Contributors role can become assignee of the issues in the project.
- Committers who have Committers role can set arbitrary roles in addition to Contributors role.
- Committers who have Administrators role can edit or delete all comments, or even delete issues in addition to Committers role.

How to set roles

1. Login to ASF JIRA
2. Go to the project page (e.g. <https://issues.apache.org/jira/browse/SUBMARINE> )
3. Hit "Administration" tab
4. Hit "Roles" tab in left side
5. Add Administrators/Committers/Contributors role

---

<a id="community-contributing"></a>

<!-- source_url: https://submarine.apache.org/docs/community/contributing/ -->

<!-- page_index: 22 -->

# How To Contribute to Submarine

Version: 0.8.0

There are several ways to contribute to Submarine:

1. Develop and Commit source code (This document will primarily focus on this.)
2. Report issues (You can report issues with both Github or Jira.)
3. Discuss/Answer questions on the mailing list
4. Share use cases

- **Apache Submarine** is an [Apache 2.0 License](https://github.com/apache/submarine/blob/master/LICENSE) Software. Contributing to Submarine means you agree to the Apache 2.0 License.
- Please read [Code of Conduct](http://www.apache.org/foundation/policies/conduct.html) carefully.
- The document [How It Works](http://www.apache.org/foundation/how-it-works.html) can help you understand Apache Software Foundation further.

- [Build From Code](#devdocs-buildfromcode)

Submarine follows [Fork & Pull](https://github.com/sevntu-checkstyle/sevntu.checkstyle/wiki/Development-workflow-with-Git:-Fork,-Branching,-Commits,-and-Pull-Request) model.

- Visit <https://github.com/apache/submarine>
- Click the `Fork` button to create a fork of the repository

```sh
# USERNAME – your Github user account name. git clone git@github.com:${USERNAME}/submarine.git
# or: git clone https://github.com/${USERNAME}/submarine.git
  
cd submarine 
# set upstream git remote add upstream git@github.com:apache/submarine.git
# or: git remote add upstream https://github.com/apache/submarine.git
 
# Don't push to the upstream master. git remote set-url --push upstream no_push
 
# Check upstream/origin:
# origin    git@github.com:${USERNAME}/submarine.git (fetch)
# origin    git@github.com:${USERNAME}/submarine.git (push)
# upstream  git@github.com:apache/submarine.git (fetch)
# upstream no_push (push) git remote -v
```

- New contributors need privilege to create JIRA issues. Public signup for Apache Jira is disabled, we need to go to [Apache Self serve sign up page](https://selfserve.apache.org/jira-account.html) to request an account.
- After Jira account created, check [Jira issue tracker](https://issues.apache.org/jira/projects/SUBMARINE/issues?filter=allopenissues) for existing issues.
- Create a new Jira issue in Submarine project. When the issue is created, a Jira number (eg. SUBMARINE-748) will be assigned to the issue automatically.
  ![jira_number_example](assets/images/jira-number-example-9d86e8dd3b72d9d9c2adddfbffc00a54_dc292a0d3b737d3b.png)

```sh
cd submarine 
 
# Make your local master up-to-date git checkout master git fetch upstream git rebase upstream/master
 
# Create a new branch fro issue SUBMARINE-${jira_number} git checkout -b SUBMARINE-${jira_number}
 
# Example: git checkout -b SUBMARINE-748
```

- You can edit the code on the `SUBMARINE-${jira_number}` branch. (Coding Style: [Code Convention](#community-contributing--code-convention))
- Create commits

```sh
git add ${edited files} 
git commit -m "SUBMARINE-${jira_number}. ${Commit Message}" 
# Example: git commit -m "SUBMARINE-748. Update Contributing guide"
```

```sh
# On SUBMARINE-${jira_number} branch git fetch upstream git rebase upstream/master
```

- Please do not use `git pull` to synchronize your local branch. Because `git pull` does a merge to create merged commits, these will make commit history messy.

```sh
git push origin SUBMARINE-${jira_number}  
```

- Visit `https://github.com/${USERNAME}/submarine/actions`
- Please make sure your new commits can pass all workflows before creating a pull request.

![check_ci_pass](assets/images/check-ci-pass-9c6656dec7130470506c7420e55c7dd0_a0873e9e40e09764.png)

- Visit your fork at `https://github.com/${USERNAME}/submarine.git`
- Click `Compare & Pull Request` button to create pull request.
  ![compare_pull_request_button](assets/images/compare-pull-request-button-a5c8f7a7ebda5fad45d1d9e6ca8ed58a_2f765c6b0addbc4e.png)

- [Pull request template](https://github.com/apache/submarine/blob/bd7578cc28f8280f9170938d4469fcc965e24a89/.github/PULL_REQUEST_TEMPLATE)
- Filling the template thoroughly can improve the speed of the review process. Example:

![pull_request_template_example](assets/images/pull-request-template-example-5db7207e23fa54cca6de32325e8d7c67_9db2de9234e2a83f.png)

- Visit <https://github.com/apache/submarine/actions>
- Please make sure your pull request can pass all workflows.

- Anyone can be a reviewer and comment on the pull requests.
- Reviewer can indicate that a patch looks suitable for merging with a comment such as: "Looks good", "LGTM", "+1". (PS: LGTM = Looks Good To Me)
- At least one indication of suitability (e.g. "LGTM") from a committer is required to be merged.
- A committer can then initiate lazy consensus ("Merge if there is no more discussion") after which the code can be merged after a particular time (usually 24 hours) if there are no more reviews.
- Contributors can ping reviewers (including committers) by commenting 'Ready to review'.

- Push new commits to SUBMARINE-${jira\_number} branch. The pull request will update automatically.
- After you address all review comments, committers will merge the pull request.

We are following Google Code style:

- [Java style](https://google.github.io/styleguide/javaguide.html)
- [Shell style](https://google.github.io/styleguide/shell.xml)

There are some plugins to format, lint your code in IDE (use [dev-support/maven-config/checkstyle.xml](hhttps://github.com/apache/submarine/blob/master/dev-support/maven-config/checkstyle.xml) as rules)

- [Checkstyle plugin for Intellij](https://plugins.jetbrains.com/plugin/1065) ([Setting Guide](http://stackoverflow.com/questions/26955766/intellij-idea-checkstyle))
- [Checkstyle plugin for Eclipse](http://eclipse-cs.sourceforge.net/#!/) ([Setting Guide](http://eclipse-cs.sourceforge.net/#!/project-setup))

---

<a id="community-howtovotecommitterorpmc"></a>

<!-- source_url: https://submarine.apache.org/docs/community/HowToVoteCommitterOrPMC/ -->

<!-- page_index: 23 -->

# How to vote a Committer or PMC

Version: 0.8.0

1. After the PMC members of Submarine discover any valuable contributions from the community contributors and obtain the consent of the candidate, they initiate a discussion on the private mailing list of Submarine:

   > [DISCUSS] YYYYY as a Submarine XXXXXX

   In the email, the source of the candidate’s contributions should be clearly stated, so that everyone can discuss and analyze. The discussion email will last at least 72 hours, and the project team members, including the mentors, will fully express their views on the proposed email.
2. Regardless of whether there is a disagreement, after the discussion email, the vote initiator needs to initiate a Committer or PMC vote on the private mailing list of Submarine;

   > [VOTE] YYYYY as a Submarine XXXXXX

   The voting mail should last for at least 72 hours, and there should be at least 3 +1 votes to pass the vote. If there are 0 votes or one -1 vote, the entire vote will fail. If voting -1, you need to clarify the question so that everyone can understand.
3. After the voting email is over, the vote initiator should summarize it on the voting line, remind the end of voting, and send it to the voting summary email.

   > [RESULTS][vote] YYYYY as a Submarine XXXXXX
4. After the vote summary email is sent, if the vote passed, the vote initiator must send an invitation email to the candidate, and the invitation email needs the candidate to reply to accept or decline through the designated mailbox.

   > [Invitation] Invitation to join Apache Submarine as a XXXXXX

   The email should be sent to the candidate, and the copy is sent to [private@submarine.apache.org](mailto:private@submarine.apache.org)
5. After the candidate accepts the invitation, if the candidate does not have an apache email account, the vote initiator needs to assist the candidate to create an apache account according to the guidelines.
6. If the above content is completed, the vote initiator still needs to do the following two things:

   6.1 Apply to the project leader to add project team members, and open the authority accounts for the jira and apache projects.

   6.2 Send a notification email to the [dev@submarine.apache.org](mailto:dev@submarine.apache.org) mail group:

   > [ANNOUNCE] New XXXXXX: YYYYY

So far, the entire process is completed, then the candidate officially becomes the Committer or PMC of Submarine.

---

<a id="community-howtobecomecommitter"></a>

<!-- source_url: https://submarine.apache.org/docs/community/HowToBecomeCommitter/ -->

<!-- page_index: 24 -->

# How to become a Committer

Version: 0.8.0

Apache Submarine builds a community completely following Apache’s rules. Apache Committer is a term used in ASF (Apache Software Foundation) to indicate the person who submits a specific project. Apache Submarine Committer has permission to write the Submarine codebase and can merge PR. Anyone who has made enough contributions to the community and gained enough trust can become an Apache Submarine Committer.

As long as anyone contributes to the Submarine project, you are the officially recognized Contributor of the Submarine project. There is no exact standard for growing from Contributor to Committer, and there is no expected timetable, but Committer candidates are generally long-term active contributors, becoming Committer does not require a huge architectural improvement contribution, or how many lines of code contribution. Contributing to the codebase, contributing to the documents, participating in the discussion of the mailing list, helping to answer questions, etc., are all ways to increase your influence.

List of potential contributions (in no particular order):

- Submit the bugs, features, and improvements you found to the issue
- Update the official documents so that the project documents are the most recent, the best practices for writing Submarine, and various useful documents for users to analyze the features.
- Perform test and report test results.
- Actively participate in voting when the version is released
- Participate in the discussion on the mailing list, usually there will be mails starting with [DISCUSS]
- Answer questions from users or developers on the mailing list
- Review the work of others (both code and non-code) and publish your own suggestions
- Review the issues on JIRA and maintain the latest status of the issues, such as closing outdated issues, changing the issue’s error information, etc.
- Guide new contributors and be familiar with the community process
- Give speeches and blogs about Submarine, and add these to the official website of Submarine
- Any contribution that is beneficial to the development of the Submarine community
  ......

More can refer to: [ASF official documents](https://community.apache.org/contributors/)

Not everyone can complete all (or even any) items on this list. If you want to contribute in other ways, then just do it (and add them to the list). Pleasant manners and dedication are all you need to have a positive impact on the Submarine project. Inviting you to become Committer is the result of your long-term and stable interaction with the community, and the trust and recognition of the Submarine community.

Committer is obliged to review and merge PRs submitted by others, test and vote on candidate versions when the version is released, participate in the discussion of feature design plans, and other types of project contributions. When you are active enough and make a bigger contribution to the community, you can be promoted to a PMC member of the Submarine project.

---

<a id="community-resources"></a>

<!-- source_url: https://submarine.apache.org/docs/community/Resources/ -->

<!-- page_index: 25 -->

# Resources

Version: 0.8.0

This document contains some resources that may help you understand more about Submarine.

<a id="community-resources--conferences"></a>

# Conferences

- **[Apache submarine: a unified machine learning platform made simple](https://dl.acm.org/doi/abs/10.1145/3517207.3526984) at EuroMLSys '22**

  - **ABSTRACT**

    As machine learning is applied more widely, it is necessary to have a machine-learning platform for both infrastructure administrators and users including expert data scientists and citizen data scientists [24] to improve their productivity. However, existing machine-learning platforms are ill-equipped to address the "Machine Learning tech debts" [36] such as glue code, reproducibility, and portability. Furthermore, existing platforms only take expert data scientists into consideration, and thus they are inflexible for infrastructure administrators and non-user-friendly for citizen data scientists. We propose Submarine, a unified machine-learning platform, and takes all infrastructure administrators, expert data scientists, and citizen data scientists into consideration. Submarine has been widely used in many technology companies, including Ke.com and LinkedIn. We present two use cases in Section 5.

---

<a id="designdocs-architecture-and-requirements"></a>

<!-- source_url: https://submarine.apache.org/docs/designDocs/architecture-and-requirements/ -->

<!-- page_index: 26 -->

# Architecture and Requirment

Version: 0.8.0

| Term | Description |
| --- | --- |
| User | A single data-scientist/data-engineer. User has resource quota, credentials |
| Team | User belongs to one or more teams, teams have ACLs for artifacts sharing such as notebook content, model, etc. |
| Admin | Also called SRE, who manages user's quotas, credentials, team, and other components. |

Everybody talks about machine learning today, and lots of companies are trying to leverage machine learning to push the business to the next level. Nowadays, as more and more developers, infrastructure software companies coming to this field, machine learning becomes more and more achievable.

In the last decade, the software industry has built many open source tools for machine learning to solve the pain points:

1. It was not easy to build machine learning algorithms manually, such as logistic regression, GBDT, and many other algorithms:
   **Answer to that:** Industries have open sourced many algorithm libraries, tools, and even pre-trained models so that data scientists can directly reuse these building blocks to hook up to their data without knowing intricate details inside these algorithms and models.
2. It was not easy to achieve "WYSIWYG, what you see is what you get" from IDEs: not easy to get output, visualization, troubleshooting experiences at the same place.
   **Answer to that:** Notebooks concept was added to this picture, notebook brought the experiences of interactive coding, sharing, visualization, debugging under the same user interface. There're popular open-source notebooks like Apache Zeppelin/Jupyter.
3. It was not easy to manage dependencies: ML applications can run on one machine is hard to deploy on another machine because it has lots of libraries dependencies.
   **Answer to that:** Containerization becomes popular and a standard to packaging dependencies to make it easier to "build once, run anywhere".
4. Fragmented tools, libraries were hard for ML engineers to learn. Experiences learned in one company are not naturally migratable to another company.
   **Answer to that:** A few dominant open-source frameworks reduced the overhead of learning too many different frameworks, concepts. Data-scientist can learn a few libraries such as Tensorflow/PyTorch, and a few high-level wrappers like Keras will be able to create your machine learning application from other open-source building blocks.
5. Similarly, models built by one library (such as libsvm) were hard to be integrated into machine learning pipeline since there's no standard format.
   **Answer to that:** Industry has built successful open-source standard machine learning frameworks such as Tensorflow/PyTorch/Keras so their format can be easily shared across. And efforts to build an even more general model format such as ONNX.
6. It was hard to build a data pipeline that flows/transform data from a raw data source to whatever required by ML applications.
   **Answer to that:** Open source big data industry plays an important role in providing, simplify, unify processes and building blocks for data flows, transformations, etc.

The machine learning industry is moving on the right track to solve major roadblocks. So what are the pain points now for companies which have machine learning needs? What can we help here? To answer this question, let's look at machine learning workflow first.

```text
1) From different data sources such as edge, clickstream, logs, etc. 
   => Land to data lakes 
 
2) From data lake, data transformation: 
   => Data transformations: Cleanup, remove invalid rows/columns, 
                            select columns, sampling, split train/test 
                            data-set, join table, etc. 
   => Data prepared for training. 
 
3) From prepared data: 
   => Training, model hyper-parameter tuning, cross-validation, etc. 
   => Models saved to storage. 
 
4) From saved models: 
   => Model assurance, deployment, A/B testing, etc. 
   => Model deployed for online serving or offline scoring. 
```

Typically data scientists responsible for item 2)-4), 1) typically handled by a different team (called Data Engineering team in many companies, some Data Engineering team also responsible for part of data transformation)

It is a complex workflow from raw data to usable models, after talking to many different data scientists, we have learned that a typical procedure to train a new model and push to production can take months to 1-2 years.

It is also a wide skill set required by this workflow. For example, data transformation needs tools like Spark/Hive for large scale and tools like Pandas for a small scale. And model training needs to be switched between XGBoost, Tensorflow, Keras, PyTorch. Building a data pipeline requires Apache Airflow or Oozie.

Yes, there are great, standardized open-source tools built for many of such purposes. But how about changes need to be made for a particular part of the data pipeline? How about adding a few columns to the training data for experiments? How about training models, and push models to validation, A/B testing before rolling to production? All these steps need jumping between different tools, UIs, and very hard to make changes, and it is not error-proof during these procedures.

To make jobs/services required by a machine learning platform to be able to run, we need an underlying resource management platform. There're some choices of resource management platform, and they have distinct advantages and disadvantages.

For example, there're many machine learning platform built on top of K8s. It is relatively easy to get a K8s from a cloud vendor, easy to orchestrate machine learning required services/daemons run on K8s. However, K8s doesn't offer good support jobs like Spark/Flink/Hive. So if your company has Spark/Flink/Hive running on YARN, there're gaps and a significant amount of work to move required jobs from YARN to K8s. Maintaining a separate K8s cluster is also overhead to Hadoop-based data infrastructure.

Similarly, if your company's data pipelines are mostly built on top of cloud resources and SaaS offerings, asking you to install a separate YARN cluster to run a new machine learning platform doesn't make a lot of sense.

In addition to the above pain, we do see Data Scientists are forced to learn underlying platform knowledge to be able to build a real-world machine learning workflow.

For most of the data scientists we talked with, they're experts of ML algorithms/libraries, feature engineering, etc. They're also most familiar with Python, R, and some of them understand Spark, Hive, etc.

If they're asked to do interactions with lower-level components like fine-tuning a Spark job's performance; or troubleshooting job failed to launch because of resource constraints; or write a K8s/YARN job spec and mount volumes, set networks properly. They will scratch their heads and typically cannot perform these operations efficiently.

TODO: Add more details.

After the data is prepared, the data scientist needs to do several routine tasks to build the ML pipeline. To get a sense of the existing the data set, it usually needs a split of the data set, the statistics of data set. These tasks have a common duplicate part of code, which reduces the efficiency of data scientists.

An abstraction layer/framework to help the developer to boost ML pipeline development could be valuable. It's better than the developer only needs to fill callback function to focus on their key logic.

<a id="designdocs-architecture-and-requirements--submarine"></a>

# Submarine

Initially, Submarine is built to solve problems of running deep learning jobs like Tensorflow/PyTorch on Apache Hadoop YARN, allows admin to monitor launched deep learning jobs, and manage generated models.

It was part of YARN initially, and code resides under `hadoop-yarn-applications`. Later, the community decided to convert it to be a subproject within Hadoop (Sibling project of YARN, HDFS, etc.) because we want to support other resource management platforms like K8s. And finally, we're reconsidering Submarine's charter, and the Hadoop community voted that it is the time to moved Submarine to a separate Apache TLP.

`ONE PLATFORM`

Submarine is the ONE PLATFORM to allow Data Scientists to create end-to-end machine learning workflow. `ONE PLATFORM` means it supports Data Scientists and data engineers to finish their jobs on the same platform without frequently switching their toolsets. From dataset exploring data pipeline creation, model training, and tuning, and push model to production. All these steps can be completed within the `ONE PLATFORM`.

`Resource Management Independent`

It is also designed to be resource management independent, no matter if you have Apache Hadoop YARN, K8s, or just a container service, you will be able to run Submarine on top it.

1) Users should be able to create, edit, delete a notebook. (P0)
2) Notebooks can be persisted to storage and can be recovered if failure happens. (P0)
3) Users can trace back to history versions of a notebook. (P1)
4) Notebooks can be shared with different users. (P1)
5) Users can define a list of parameters of a notebook (looks like parameters of the notebook's main function) to allow executing a notebook like a job. (P1)
6) Different users can collaborate on the same notebook at the same time. (P2)

A running notebook instance is called notebook session (or session for short).

Experiments of Submarine is an offline task. It could be a shell command, a Python command, a Spark job, a SQL query, or even a workflow.

The primary purposes of experiments under Submarine's context is to do training tasks, offline scoring, etc. However, experiment can be generalized to do other tasks as well.

Major requirement of experiment:

1) Experiments can be submitted from UI/CLI/SDK.
2) Experiments can be monitored/managed from UI/CLI/SDK.
3) Experiments should not bind to one resource management platform (K8s).

![](assets/images/experiments-7a09831687ecbc0e1dcf01b0c6f45445_ccc28c83245fac8a.png)

There're two types of experiments:
`Adhoc experiments`: which includes a Python/R/notebook, or even an adhoc Tensorflow/PyTorch task, etc.

`Predefined experiment library`: This is specialized experiments, which including developed libraries such as CTR, BERT, etc. Users are only required to specify a few parameters such as input, output, hyper parameters, etc. Instead of worrying about where's training script/dependencies located.

Requirements:

- Allow run adhoc scripts.
- Allow model engineer, data scientist to run Tensorflow/Pytorch programs on K8s/Container-cloud.
- Allow jobs easy access data/models in HDFS/s3, etc.
- Support run distributed Tensorflow/Pytorch jobs with simple configs.
- Support run user-specified Docker images.
- Support specify GPU and other resources.

Here's an example of predefined experiment library to train deepfm model:

```text
{"input": {"train_data": ["hdfs:///user/submarine/data/tr.libsvm"],"valid_data": ["hdfs:///user/submarine/data/va.libsvm"],"test_data": ["hdfs:///user/submarine/data/te.libsvm"],"type": "libsvm" },"output": {"save_model_dir": "hdfs:///user/submarine/deepfm","metric": "auc" },"training": {"batch_size" : 512,"field_size": 39,"num_epochs": 3,"feature_size": 117581,...}}
```

Predefined experiment libraries can be shared across users on the same platform, users can also add new or modified predefined experiment library via UI/REST API.

We will also model AutoML, auto hyper-parameter tuning to predefined experiment library.

Pipeline is a special kind of experiment:

- A pipeline is a DAG of experiments.
- Can be also treated as a special kind of experiment.
- Users can submit/terminate a pipeline.
- Pipeline can be created/submitted via UI/API.

Environment profiles (or environment for short) defines a set of libraries and when Docker is being used, a Docker image in order to run an experiment or a notebook.

Docker or VM image (such as AMI: Amazon Machine Images) defines the base layer of the environment.

On top of that, users can define a set of libraries (such as Python/R) to install.

Users can save different environment configs which can be also shared across the platform. Environment profiles can be used to run a notebook (e.g. by choosing different kernel from Jupyter), or an experiment. Predefined experiment library includes what environment to use so users don't have to choose which environment to use.

Environments can be added/listed/deleted/selected through CLI/SDK.

- Model artifacts are generated by experiments or notebook.
- A model consists of artifacts from one or multiple files.
- Users can choose to save, tag, version a produced model.
- Once The Model is saved, Users can do the online model serving or offline scoring of the model.

After model saved, users can specify a serving script, a model and create a web service to serve the model.

We call the web service to "endpoint". Users can manage (add/stop) model serving endpoints via CLI/API/UI.

Submarine-SDK provides tracking/metrics APIs, which allows developers to add tracking/metrics and view tracking/metrics from Submarine Workbench UI.

Submarine Services (See architecture overview below) should be deployed easily on-prem / on-cloud. Since there're more and more public cloud offering for compute/storage management on cloud, we need to support deploy Submarine compute-related workloads (such as notebook session, experiments, etc.) to cloud-managed clusters.

This also include Submarine may need to take input parameters from customers and create/manage clusters if needed. It is also a common requirement to use hybrid of on-prem/on-cloud clusters.

There're 4 kinds of objects need access-control:

- Assets belong to Submarine system, which includes notebook, experiments and results, models, predefined experiment libraries, environment profiles.
- Data security. (Who owns what data, and what data can be accessed by each users).
- User credentials. (Such as LDAP).
- Other security, such as Git repo access, etc.

For the data security / user credentials / other security, it will be delegated to 3rd libraries such as Apache Ranger, IAM roles, etc.

Assets belong to Submarine system will be handled by Submarine itself.

Here're operations which Submarine admin can do for users / teams which can be used to access Submarine's assets.

**Operations for admins**

- Admin uses "User Management System" to onboard new users, upload user credentials, assign resource quotas, etc.
- Admins can create new users, new teams, update user/team mappings. Or remove users/teams.
- Admin can set resource quotas (if different from system default), permissions, upload/update necessary credentials (like Kerberos keytab) of a user.
- A DE/DS can also be an admin if the DE/DS has admin access. (Like a privileged user). This will be useful when a cluster is exclusively shared by a user or only shared by a small team.
- `Resource Quota Management System` helps admin to manage resources quotas of teams, organizations. Resources can be machine resources like CPU/Memory/Disk, etc. It can also include non-machine resources like $$-based budgets.

There's also need to tag dataset which will be used for training and shared across the platform by different users.

Like mentioned above, access to the actual data will be handled by 3rd party system like Apache Ranger / Hive Metastore which is out of the Submarine's scope.

```text
     +-----------------------------------------------------------------+ 
     |            Submarine UI / CLI / REST API / SDK                  | 
     |                 Mini-Submarine                                  | 
     +-----------------------------------------------------------------+ 
 
     +--------------------Submarine Server-----------------------------+ 
     | +---------+ +---------+ +----------+ +----------+ +------------+| 
     | |Data set | |Notebooks| |Experiment| |Models    | |Servings    || 
     | +---------+ +---------+ +----------+ +----------+ +------------+| 
     |-----------------------------------------------------------------| 
     |                                                                 | 
     | +-----------------+ +-----------------+ +---------------------+ | 
     | |Experiment       | |Compute Resource | |Other Management     | | 
     | |Manager          | |   Manager       | |Services             | | 
     | +-----------------+ +-----------------+ +---------------------+ | 
     |   Spark, template      K8s/Docker                          | 
     |   TF, PyTorch, pipeline                                         | 
     |                                                                 | 
     + +-----------------+                                             + 
     | |Submarine Meta   |                                             | 
     | |    Store        |                                             | 
     | +-----------------+                                             | 
     |                                                                 | 
     +-----------------------------------------------------------------+ 
 
      (You can use http://stable.ascii-flow.appspot.com/#Draw 
      to draw such diagrams) 
```

`Compute Resource Manager` Helps to manage compute resources on-prem/on-cloud, this module can also handle cluster creation / management, etc.

`Experiment Manager` Work with "Compute Resource Manager" to submit different kinds of workloads such as (distributed) Tensorflow / Pytorch, etc.

`Submarine SDK` provides Java/Python/REST API to allow DS or other engineers to integrate into Submarine services. It also includes a `mini-submarine` component that launches Submarine components from a single Docker container (or a VM image).

Details of Submarine Server design can be found at [submarine-server-design](#designdocs-submarine-server-architecture).

---

<a id="designdocs-implementation-notes"></a>

<!-- source_url: https://submarine.apache.org/docs/designDocs/implementation-notes/ -->

<!-- page_index: 27 -->

# Implementation Notes

Version: 0.8.0

Before digging into details of implementations, you should read [architecture-and-requirements](#designdocs-architecture-and-requirements) first to understand overall requirements and architecture.

Here're sub topics of Submarine implementations:

- [Submarine Storage](#designdocs-storage-implementation): How to store metadata, logs, metrics, etc. of Submarine.
- [Submarine Environment](#designdocs-environments-implementation): How environments created, managed, stored in Submarine.
- [Submarine Experiment](#designdocs-experiment-implementation): How experiments managed, stored, and how the predefined experiment template works.
- [Submarine Notebook](#designdocs-notebook-implementation): How experiments managed, stored, and how the predefined experiment template works.
- [Submarine Server](#designdocs-submarine-server-architecture): How Submarine server is designed, architecture, implementation notes, etc.

Working-in-progress designs, Below are designs which are working-in-progress, we will move them to the upper section once design & review is finished:

- [Submarine services deployment module:](#designdocs-wip-designs-submarine-launcher) How to deploy submarine services to k8s or cloud.

---

<a id="designdocs-environments-implementation"></a>

<!-- source_url: https://submarine.apache.org/docs/designDocs/environments-implementation/ -->

<!-- page_index: 28 -->

# Environments Implementation

Version: 0.8.0

Environment profiles (or environment for short) defines a set of libraries and when Docker is being used, a Docker image in order to run an experiment or a notebook.

Docker and/or VM-image (such as, VirtualBox/VMWare images, Amazon Machine Images - AMI, Or custom image of Azure VM) defines the base layer of the environment. Please note that VM-image is different from VM instance type,

On top of that, users can define a set of libraries (such as Python/R) to install, we call it kernel.

**Example of Environment**

```text
+-------------------+ |+-----------------+| || Python=3.7      || || Tensorflow=2.0  || |+---Exp Dependency+| |+-----------------+| ||OS=Ubuntu16.04   || ||CUDA=10.2        || ||GPU_Driver=375.. || |+---Base Library--+| +-------------------+
```

As you can see, There're base libraries, such as what OS, CUDA version, GPU driver, etc. They can be achieved by specifying a VM-image / Docker image.

On top of that, user can bring their dependencies, such as different version of Python, Tensorflow, Pandas, etc.

**How users use environment?**

Users can save different environment configs which can be also shared across the platform. Environment profiles can be used to run a notebook (e.g. by choosing different kernel from Jupyter), or an experiment. Predefined experiment library includes what environment to use so users don't have to choose which environment to use.

```text
 
        +-------------------+ 
        |+-----------------+|       +------------+ 
        || Python=3.7      ||       |User1       | 
        || Tensorflow=2.0  ||       +------------+ 
        |+---Kernel -------+|       +------------+ 
        |+-----------------+|<----+ |User2       | 
        ||OS=Ubuntu16.04   ||     + +------------+ 
        ||CUDA=10.2        ||     | +------------+ 
        ||GPU_Driver=375.. ||     | |User3       | 
        |+---Base Library--+|     | +------------+ 
        +-----Default-Env---+     | 
                                  | 
                                  | 
        +-------------------+     | 
        |+-----------------+|     | 
        || Python=3.3      ||     | 
        || Tensorflow=2.0  ||     | 
        |+---kernel--------+|     | 
        |+-----------------+|     | 
        ||OS=Ubuntu16.04   ||     | 
        ||CUDA=10.3        ||<----+ 
        ||GPU_Driver=375.. || 
        |+---Base Library--+| 
        +-----My-Customized-+ 
```

There're two environments in the above graph, "Default-Env" and "My-Customized", which can have different combinations of libraries for different experiments/notebooks. Users can choose different environments for different experiments as they want.

Environments can be added/listed/deleted/selected through CLI/SDK/UI.

<a id="designdocs-environments-implementation--implementation"></a>

# Implementation

Let look at what object definition looks like to define an environment, API of environment looks like:

```text
    name: "my_submarine_env", 
    vm-image: "...", 
    docker-image: "...",  
    kernel:  
       <object of kernel> 
    description: "this is the most common env used by team ABC" 
```

- `vm-image` is optional if we don't need to launch new VM (like running a training job in a cloud-remote machine).
- `docker-image` is required
- `kernel` could be optional if kernel is already included by vm-image or docker-image.
- `name` of the environment should be unique in the system, so user can reference it when create a new experiment/notebook.

Docker-image and VM image should be prepared by system admin / SREs, it is hard for Data-Scientists to write an error-proof Dockerfile, and push/manage Docker images. This is one of the reason we hide Docker-image inside "environment", we will encourage users to customize their kernels if needed, but don't have to touch Dockerfile and build/push/manage new Docker images.

As a project, we will document what's the best practice and example of Dockerfiles.

Dockerfile should include proper `ENTRYPOINT` definition which pointed to our default script, so no matter it is notebook, or an experiment, we will setup kernel (see below) and other environment variables properly.

After investigating different alternatives (such as pipenv, venv, etc.), we decided to use Conda environment which nicely replaces Python virtual env, pip, and can also support other languages. More details can be found at: <https://medium.com/@krishnaregmi/pipenv-vs-virtualenv-vs-conda-environment-3dde3f6869ed>

When once Conda, users can easily add, remove dependency of a Conda environment. User can also easily export environment to yaml file.

The yaml file of Conda environment by using `conda env export` looks like:

```text
name: base 
channels: 
  - defaults 
dependencies: 
  - _ipyw_jlab_nb_ext_conf=0.1.0=py37_0 
  - alabaster=0.7.12=py37_0 
  - anaconda=2020.02=py37_0 
  - anaconda-client=1.7.2=py37_0 
  - anaconda-navigator=1.9.12=py37_0 
  - anaconda-project=0.8.4=py_0 
  - applaunchservices=0.2.1=py_0 
```

Including Conda kernel, the environment object may look like:

```text
name: "my_submarine_env", 
    vm-image: "...", 
    docker-image: "...",  
    kernel:  
      name: team_default_python_3.7 
      channels: 
        - defaults 
      dependencies: 
        - _ipyw_jlab_nb_ext_conf=0.1.0=py37_0 
        - alabaster=0.7.12=py37_0 
        - anaconda=2020.02=py37_0 
        - anaconda-client=1.7.2=py37_0 
        - anaconda-navigator=1.9.12=py37_0 
```

When launch a new experiment / notebook session using the `my_submarine_env`, submarine server will use defined Docker image, and Conda kernel to launch of container.

Environment of Submarine is just a simple text file, so it will be persisted in Submarine metastore, which is ideally a Database.

Docker image is stored inside a regular Docker registry, which will be handled outside of the system.

Conda dependencies are stored in Conda channel (where referenced packages are stored), which will be handled/setuped separately. (Popular conda channels are `default` and `conda-forge`)

For more detailed discussion about storage-related implementations, please refer to [storage-implementation](#designdocs-storage-implementation).

We like simplicities, and we don't want to leak complexities of implementations to the users. To make it happen, we have to do some works to hide complexities.

There're two primary uses of environments: experiments and notebook, for both of them, users should not do works like explictily call `conda active $env_name` to active environments. To make it happen, what we can do is to include following parts in Dockerfile

```text
FROM ubuntu:18.04 
 
<Include whatever base-libraries like CUDA, etc.> 
 
<Make sure conda (with our preferred version) is installed> 
<Make sure Jupyter (with our preferred version) is installed> 
 
# This is just a sample of Dockerfile, users can do more customizations if needed 
ENTRYPOINT ["/submarine-bootstrap.sh"] 
```

When Submarine Server (this is implementation detail of Submarine Server, user will not see it at all) launch an experiment, or notebook, it will invoke following `docker run` command (or any other equvilant like using K8s spec):

```text
docker run <submarine_docker_image> --kernel <kernel_name> -- .... python train.py --batch_size 5 (and other parameters) 
```

Similarily, to launch a notebook:

```text
docker run <submarine_docker_image> --kernel <kernel_name> -- .... jupyter 
```

The `submarine-bootstrap.sh` is part of Submarine repo, and will handle `--kernel` argument which will invoke `conda active $kernel_name` before anything else. (Like run the training job).

---

<a id="designdocs-experiment-implementation"></a>

<!-- source_url: https://submarine.apache.org/docs/designDocs/experiment-implementation/ -->

<!-- page_index: 29 -->

# Experiment Implementation

Version: 0.8.0

This document talks about implementation of experiment, flows and design considerations.

Experiment consists of following components, also interact with other Submarine or 3rd-party components, showing below:

```text
+---------------------------------------+ +----------+ |      Experiment Tasks                 | |Run       | |                                       | |Configs   | | +----------------------------------+  | +----------+ | |   Experiment Runnable Code       |  | +-----------------+ +----------+ | |                                  |  | |Output Artifacts | |Input Data| | |     (Like train-job.py)          |  | |(Models, etc.)   | |          | | +----------------------------------+  | +-----------------+ |          | | +----------------------------------+  | +----------+ | |   Experiment Deps (Like Python)  |  | +-------------+ | +----------------------------------+  | |Logs/Metrics | | +----------------------------------+  | |             | | |  OS, Base Libaries (Like CUDA)   |  | +-------------+ | +----------------------------------+  | +---------------------------------------+ ^ | (Launch Task with resources) + +---------------------------------+ |Resource Manager (K8s/Cloud)| +---------------------------------+
```

As showing in the above diagram, Submarine experiment consists of the following items:

- On the left side, there're input data and run configs.
- In the middle box, they're experiment tasks, it could be multiple tasks when we run distributed training, pipeline, etc.
  - There're main runnable code, such as `train.py` for the training main entry point.
  - The two boxes below: experiment dependencies and OS/Base libraries we called `Submarine Environment Profile` or `Environment` for short. Which defined what is the basic libraries to run the main experiment code.
  - Experiment tasks are launched by Resource Manager, such as K8s/Cloud or just launched locally. There're resources constraints for each experiment tasks. (e.g. how much memory, cores, GPU, disk etc. can be used by tasks).
- On the right side, they're artifacts generated by experiments:
  - Output artifacts: Which are main output of the experiment, it could be model(s), or output data when we do batch prediction.
  - Logs/Metrics for further troubleshooting or understanding of experiment's quality.

For the rest of the design doc, we will talk about how we handle environment, code, and manage output/logs, etc.

This is not a full definition of experiment, for more details, please reference to experiment API.

Here's just an example of experiment object which help developer to understand what included in an experiment.

```yaml
experiment: 
       name: "abc", 
       type: "script", 
       environment: "team-default-ml-env" 
       code: 
           sync_mode: s3 
           url: "s3://bucket/training-job.tar.gz" 
       parameter: > python training.py --iteration 10 
                    --input=s3://bucket/input output=s3://bucket/output 
       resource_constraint: 
           res="mem=20gb, vcore=3, gpu=2" 
       timeout: "30 mins" 
```

This defined a "script" experiment, which has a name "abc", the name can be used to track the experiment. There's environment "team-default-ml-env" defined to make sure dependencies of the job can be downloaded properly before executing the job.

`code` defined where the experiment code will be downloaded, we will support a couple of sync\_mode like s3 (or abfs/hdfs), git, etc.

Different types of experiments will have different specs, for example distributed Tensorflow spec may look like:

```yaml
experiment: 
       name: "abc-distributed-tf", 
       type: "distributed-tf", 
       ps: 
            environment: "team-default-ml-cpu" 
            resource_constraint: 
                 res="mem=20gb, vcore=3, gpu=0" 
       worker: 
            environment: "team-default-ml-gpu" 
            resource_constraint: 
                 res="mem=20gb, vcore=3, gpu=2" 
       code: 
           sync_mode: git 
           url: "https://foo.com/training-job.git" 
       parameter: > python /code/training-job/training.py --iteration 10 
                    --input=s3://bucket/input output=s3://bucket/output 
       tensorboard: enabled 
       timeout: "30 mins" 
```

Since we have different Docker image, one is using GPU and one is not using GPU, we can specify different environment and resource constraint.

Please refer to [environment-implementation.md](#designdocs-environments-implementation) for more details

There're different types of storage, such as logs, metrics, dependencies (environments). For more details. Please refer to [storage-implementations](#designdocs-storage-implementation) for more details. This also includes how to manage code for experiment code.

To better understand experiment implementation, It will be good to understand what is the steps of experiment submission.

*Please note that below code is just pseudo code, not official APIs.*

Before submit the environment, you have to choose what environment to choose. Environment defines dependencies, etc. of an experiment or a notebook. might looks like below:

```text
conda_environment = 
""" 
  name: conda-env 
  channels: 
    - defaults 
  dependencies: 
    - asn1crypto=1.3.0=py37_0 
    - blas=1.0=mkl 
    - ca-certificates=2020.1.1=0 
    - certifi=2020.4.5.1=py37_0 
    - cffi=1.14.0=py37hb5b8e2f_0 
    - chardet=3.0.4=py37_1003 
  prefix: /opt/anaconda3/envs/conda-env 
""" 
 
# This environment can be different from notebook's own environment 
environment = create_environment { 
    DockerImage = "ubuntu:16", 
    CondaEnvironment = conda_environment 
} 
```

To better understand how environment works, please refer to [environment-implementation](#designdocs-environments-implementation).

For ad-hoc experiment (code located at S3), assume training code is part of the `training-job.tar.gz` and main class is `train.py`. When the job is launched, whatever specified in the localize\_artifacts will be downloaded.

```text
experiment = create_experiment {Environment = environment,ExperimentConfig = {type = "adhoc",localize_artifacts = ["s3://bucket/training-job.tar.gz" ],name = "abc",parameter = "python training.py --iteration 10 --input="s3://bucket/input output="s3://bucket/output",}} experiment.run() experiment.wait_for_finish(print_output=True)
```

It is possible we want to run a notebook file in offline mode, to do that, here's code to use to run a notebook code

```text
experiment = create_experiment {Environment = environment,ExperimentConfig = {type = "adhoc",localize_artifacts = ["s3://bucket/folder/notebook-123.ipynb" ],name = "abc",parameter = "runipy training.ipynb --iteration 10 --input="s3://bucket/input output="s3://bucket/output",}} experiment.run() experiment.wait_for_finish(print_output=True)
```

```text
experiment = create_experiment {# Here you can use default environment of library Environment = environment,ExperimentConfig = {type = "template",name = "abc",# A unique name of template template = "deepfm_ctr",# yaml file defined what is the parameters need to be specified.parameter = {Input: "S3://.../input",Output: "S3://.../output" Training: {"batch_size": 512,"l2_reg": 0.01,...}}}} experiment.run() experiment.wait_for_finish(print_output=True)
```

There's a common misunderstanding about what is the differences between running experiment v.s. running task from a notebook session. We will talk about differences and commonalities:

**Differences**

|  | Experiment | Notebook Session |
| --- | --- | --- |
| Run mode | Offline | Interactive |
| Output Artifacts (a.k.a model) | Persisted in a shared storage (like S3/NFS) | Local in the notebook session container, could be ephemeral |
| Run history (meta, logs, metrics) | Meta/logs/metrics can be traced from experiment UI (or corresponding API) | No run history can be traced from Submarine UI/API. Can view the current running paragraph's log/metrics, etc. |
| What to run? | Code from Docker image or shared storage (like Tarball on S3, Github, etc.) | Local in the notebook's paragraph |

**Commonalities**

|  | Experiment & Notebook Session |
| --- | --- |
| Environment | They can share the same Environment configuration |

(Please refer to [architecture of submarine server](#designdocs-submarine-server-architecture) for more details)

The experiment manager receives the experiment requests, persisting the experiment metas in a database(e.g. MySQL), will invoke subsequence modules to submit and monitor the experiment's execution.

After experiment accepted by experiment manager, based on which cluster the experiment intended to run (like mentioned in the previous sections, Submarine supports to manage multiple compute clusters), compute cluster manager will returns credentials to access the compute cluster. It will also be responsible to create a new compute cluster if needed.

For most of the on-prem use cases, there's only one cluster involved, for such cases, ComputeClusterManager returns credentials to access local cluster if needed.

Experiment Submitter handles different kinds of experiments to run (e.g. ad-hoc script, distributed TF, MPI, pre-defined templates, Pipeline, AutoML, etc.). And such experiments can be managed by different resource management systems (e.g. K8s, container cloud, etc.)

To meet the requirements to support variant kinds of experiments and resource managers, we choose to use plug-in modules to support different submitters (which requires jars to submarine-server’s classpath).

To avoid jars and dependencies of plugins break the submarine-server, the plug-ins manager, or both. To solve this issue, we can instantiate submitter plug-ins using a classloader that is different from the system classloader.

Each plug-in uses a separate module under the server-submitter module. As the default implements, we provide for K8s.

The submitter-k8s plug-in is used to submit the job to Kubernetes cluster and use the [operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) as the runtime. The submitter-k8s plug-in implements the operation of CRD object and provides the java interface. In the beginning, we use the [tf-operator](https://github.com/kubeflow/tf-operator) for the TensorFlow.

If Submarine want to support the other resource management system in the future, such as submarine-docker-cluster (submarine uses the Raft algorithm to create a docker cluster on the docker runtime environment on multiple servers, providing the most lightweight resource scheduling system for small-scale users). We should create a new plug-in module named submitter-docker under the server-submitter module.

The monitor tracks the experiment life cycle and records the main events and key info in runtime. As the experiment run progresses, the metrics are needed for evaluation of the ongoing success or failure of the execution progress. Due to adapt the different cluster resource management system, so we need a generic metric info structure and each submitter plug-in should inherit and complete it by itself.

```text
 +-----------------+  +----------------+ +----------------+ +-----------------+ 
 |Experiments      |  |Compute Cluster | |Experiment      | | Experiment      | 
 |Mgr              |  |Mgr             | |Submitter       | | Monitor         | 
 +-----------------+  +----------------+ +----------------+ +-----------------+ 
          +                    +                  +                  + 
 User     |                    |                  |                  | 
 Submit   |+------------------------------------->+                  + 
 Xperiment|          Use submitter.validate(spec) |                  | 
          |          to validate spec and create  |                  | 
          |          experiment object (state-    |                  | 
          |          machine).                    |                  | 
          |                                       |                  | 
          |          The experiment manager will  |                  | 
          |          persist meta-data to Database|                  | 
          |                    |                  |                  | 
          |                    |                  +                  + 
          |+-----------------> +                  |                  | 
          |  Submit Experiments|                  |                  | 
          |   To ComputeCluster|                  |                  | 
          |   Mgr, get existing|+---------------->|                  | 
          |   cluster, or      |  Use Submitter   |                  | 
          |   create a new one.|  to submit       |+---------------> | 
          |                    |  Different kinds |  Once job is     | 
          |                    |  of experiments  |  submitted, use  |+----+ 
          |                    |  to k8s, etc|  monitor to get  |     | 
          |                    |                  |  status updates  |     | 
          |                    |                  |                  |     | Monitor 
          |                    |                  |                  |     | Xperiment 
          |                    |                  |                  |     | status 
          |                    |                  |                  |     | 
          |<--------------------------------------------------------+|     | 
          |                    |                  |                  |     | 
          |                  Update Status back to Experiment        |     | 
          |                    |      Manager     |                  |<----+ 
          |                    |                  |                  | 
          |                    |                  |                  | 
          |                    |                  |                  | 
          v                    v                  v                  v 
```

TODO: add more details about template, environment, etc.

Experiment/notebook-session/model-serving share a lot of commonalities, all of them are:

- Some workloads running on K8s.
- Need persist meta data to DB.
- Need monitor task/service running status from resource management system.

We need to make their implementation are loose-coupled, but at the same time, share some building blocks as much as possible (e.g. submit PodSpecs to K8s, monitor status, get logs, etc.) to reduce duplications.

Predefined Experiment Template is just a way to save data-scientists time to repeatedly entering parameters which is not error-proof and user experience is also bad.

Predefined experiment template consists a list of parameters, each of the parameter has 4 properties:

| Key | Required | Default Value | Description |
| --- | --- | --- | --- |
| Name of the key | true/false | When required = false, a default value can be provided by the template | Description of the parameter |

For the example of deepfm CTR training experiment mentioned in the [architecture-and-requirements.md](#designdocs-architecture-and-requirements)

```text
{"input": {"train_data": ["hdfs:///user/submarine/data/tr.libsvm"],"valid_data": ["hdfs:///user/submarine/data/va.libsvm"],"test_data": ["hdfs:///user/submarine/data/te.libsvm"],"type": "libsvm" },"output": {"save_model_dir": "hdfs:///user/submarine/deepfm","metric": "auc" },"training": {"batch_size" : 512,"field_size": 39,"num_epochs": 3,"feature_size": 117581,...}}
```

The template will be (in yaml format):

```yaml
# deepfm.ctr template 
name: deepfm.ctr 
author: 
description: > 
  This is a template to run CTR training using deepfm algorithm, by default it runs 
  single node TF job, you can also overwrite training parameters to use distributed 
  training. 
 
parameters: 
  - name: input.train_data 
    required: true 
    description: > 
      train data is expected in SVM format, and can be stored in HDFS/S3 
    ... 
  - name: training.batch_size 
    required: false 
    default: 32 
    description: This is batch size of training 
```

The batch format can be used in UI/API.

Please note that, the conversion of predefined-experiment-template will be always handled by server. The invoke flow looks like:

```text
 
                         +------------Submarine Server -----------------------+ 
   +--------------+      |  +-----------------+                               | 
   |Client        |+------->|Experimment Mgr  |                               | 
   |              |      |  |                 |                               | 
   +--------------+      |  +-----------------+                               | 
                         |          +                                         | 
          Submit         |  +-------v---------+       Get Experiment Template | 
          Template       |  |Experiment       |<-----+From pre-registered     | 
          Parameters     |  |Template Registry|       Templates               | 
          to Submarine   |  +-------+---------+                               | 
          Server         |          |                                         | 
                         |  +-------v---------+       +-----------------+     | 
                         |  |Deepfm CTR Templ-|       |Experiment-      |     | 
                         |  |ate Handler      +------>|Tensorflow       |     | 
                         |  +-----------------+       +--------+--------+     | 
                         |                                     |              | 
                         |                                     |              | 
                         |                            +--------v--------+     | 
                         |                            |Experiment       |     | 
                         |                            |Submitter        |     | 
                         |                            +--------+--------+     | 
                         |                                     |              | 
                         |                                     |              | 
                         |                            +--------v--------+     | 
                         |                            |                 |     | 
                         |                            | ......          |     | 
                         |                            +-----------------+     | 
                         |                                                    | 
                         +----------------------------------------------------+ 
```

Basically, from Client, it submitted template parameters to Submarine Server, inside submarine server, it finds the corresponding template handler based on the name. And the template handler converts input parameters to an actual experiment, such as a distributed TF experiment. After that, it goes the similar route to validate experiment spec, compute cluster manager, etc. to get the experiment submitted and monitored.

Predefined-experiment-template is able to create any kind of experiment, it could be a pipeline:

```text
 
   +-----------------+                  +------------------+ 
   |Template XYZ     |                  | XYZ Template     | 
   |                 |+---------------> | Handler          | 
   +-----------------+                  +------------------+ 
                                                   + 
                                                   | 
                                                   | 
                                                   | 
                                                   | 
                                                   v 
             +--------------------+      +------------------+ 
             | +-----------------+|      | Predefined       | 
             | |  Split Train/   ||<----+| Pipeline         | 
             | |  Test data      ||      +------------------+ 
             | +-------+---------+| 
             |         |          | 
             | +-------v---------+| 
             | |  Spark Job ETL  || 
             | |                 || 
             | +-------+---------+| 
             |         |          | 
             | +-------v---------+| 
             | | Train using     || 
             | | XGBoost         || 
             | +-------+---------+| 
             |         |          | 
             | +-------v---------+| 
             | | Validate Train  || 
             | | Results         || 
             | +-----------------+| 
             |                    | 
             +--------------------+ 
```

Template can be also chained to reuse other template handlers

```text
 
   +-----------------+                  +------------------+ 
   |Template XYZ     |                  | XYZ Template     | 
   |                 |+---------------> | Handler          | 
   +-----------------+                  +------------------+ 
                                                   + 
                                                   | 
                                                   v 
               +------------------+      +------------------+ 
               |Distributed       |      | ABC Template     | 
               |TF Experiment     |<----+| Handler          | 
               +------------------+      +------------------+ 
```

Template Handler is a callable class inside Submarine Server with a standard interface defined like.

```java
interface ExperimentTemplateHandler { 
   ExperimentSpec createExperiment(TemplatedExperimentParameters param) 
} 
```

We should avoid users to do coding when they want to add new template, we should have several standard template handler to deal with most of the template handling.

Experiment templates can be registered/updated/deleted via Submarine Server's REST API, which need to be discussed separately in the doc. (TODO)

---

<a id="designdocs-notebook-implementation"></a>

<!-- source_url: https://submarine.apache.org/docs/designDocs/notebook-implementation/ -->

<!-- page_index: 30 -->

# Notebook Implementation

Version: 0.8.0

Users can start N (N >= 0) number of Notebook sessions, a notebook session is a running notebook instance.

- Notebook session can be launched by Submarine UI (P0), and Submarine CLI (P2).
- When launch notebook session, users can choose T-shirt size of notebook session (how much mem/cpu/gpu resources, or resource profile such as small, medium, large, etc.). (P0)
- And user can choose an environment for notebook. More details please refer to [environment implementation](#designdocs-environments-implementation) (P0)
- When start a notebook, user can choose what code to be initialized, similar to experiment. (P1)
- Optionally, users can choose to attach a persistent volume to a notebook session. (P2)

Users can get a list of notebook sessions belongs to themselves, and connect to notebook session.

User can choose to terminate a running notebook session.

- How many concurrent notebook sessions can be launched by each user is determined by resource quota limits of each user, and maximum concurrent notebook sessions can be launched by each user. (P2)

Running notebook sessions' metadata need persistented in Submarine's metadata store (Database).

```text
 
  +--------------+  +--------Submarine Server--------------------+ 
  |Submarine UI  |  | +-------------------+                      | 
  |              |+--->  Submarine        |                      | 
  |  Notebook    |  | |  Notebook REST API|                      | 
  +--------------+  | |                   |                      | 
                    | +--------+----------+     +--------------+ | 
                    |          |             +->|Metastore     | | 
                    | +--------v----------+  |  |DB            | | 
                    | | Submarine         +--+  +--------------+ | 
                    | | Notebook Mgr      |                      | 
                    | |                   |                      | 
                    | |                   |                      | 
                    | +--------+----------+                      | 
                    |          |                                 | 
                    +----------|---------------------------------+ 
                               | 
                +--------------+ 
       +--------v---------+ 
       | Notebook Session | 
       |                  | 
       |   instance       | 
       |                  | 
       +------------------+ 
```

Once user use Submarine UI to launch a notebook session, Submarine notebook manager inside Submarine Server will persistent notebook session's metadata, and launch a new notebook session instance.

When using K8s as resource manager, Submarine notebook session will run as a new POD.

There're several different types of storage requirements for Submarine notebook.

For code, environment, etc, storage, please refer to [storage implementation](#designdocs-storage-implementation), check "Localization of experiment/notebook/model-serving code".

When there're needs to attach volume (such as user's home folder) to Submarine notebook session, please check [storage implementation](#designdocs-storage-implementation), check "Attachable volume".

Submarine notebook's environment should be used to run experiment, model serving, etc. Please check [environment implementation](#designdocs-environments-implementation). (More specific to notebook, please check "How to implement to make user can easily use Submarine environments")

Please note that notebook's Environment should include right version of notebook libraries, and admin should follow the guidance to build correct Docker image, Conda libraries to correctly run Notebook.

Users can run new experiment, access metrics information, or do model operations using Submarine SDK.

Submarine SDK is a Python library which can talk to Submarine Server which need Submarine Server's endpoint as well as user credentials.

To ensure better experience, we recommend always install proper version of Submarine SDK from environment which users can use Submarine SDK directly from commandline. (We as Submarine community can provide sample Dockerfile or Conda environment which have correct base libraries installed for Submarine SDK).

Submarine Server IP will be configured automatically by Submarine Server, and added as an envar when Submarine notebook session got launched.

Please refer to [Security Implementation](#designdocs-wip-designs-security-implementation)

Once user accessed to a running notebook session, the user can also access resources of the notebook, capability of submit new experiment, and access data. This is also very dangerous so we have to protect it.

A simple solution is to use token-based authentication <https://jupyter-notebook.readthedocs.io/en/stable/security.html>. A more common way is to use solutions like KNOX to support SSO.

We need expand this section to more details. (TODO).

---

<a id="designdocs-storage-implementation"></a>

<!-- source_url: https://submarine.apache.org/docs/designDocs/storage-implementation/ -->

<!-- page_index: 31 -->

# Storage Implementation

Version: 0.8.0

First let's look at what user will interact for most of the time:

- Notebook
- Experiment
- Model Servings

```text
+---------+    +------------+ |Logs     |<--+|Notebook    | +----------+            +---------+    +------------+     +----------------+ |Trackings |                        <-+|Experiment  |<--+>|Model Artifacts | +----------+     +-----------------+   +------------+     +----------------+ +----------+<---+|ML-related Metric|<--+Servings    | |tf.events |     +-----------------+   +------------+ +----------+                                 ^              +-----------------+ +              | Environments    | +----------------------+  |                 | +-----------------+         | Submarine Metastore  |  |  Dependencies   | |Code             |         +----------------------+  |                 | +-----------------+         |Experiment Meta       |  |   Docker Images | +----------------------+  +-----------------+ |Model Store Meta      | +----------------------+ |Model Serving Meta    | +----------------------+ |Notebook meta         | +----------------------+ |Experiment Templates  | +----------------------+ |Environments Meta     | +----------------------+
```

First of all, all the notebook-sessions / experiments / model-serving instances) are more or less interact with following storage objects:

- Logs for these tasks for troubleshooting.
- ML-related metrics such as loss, epoch, etc. (in contrast of system metrics such as CPU/memory usage, etc.)
  - There're different types of ML-related metrics, for Tensorflow/pytorch, they can use tf.events and get visualizations on tensorboard.
  - Or they can use tracking APIs (such as Submarine tracking, mlflow tracking, etc.) to output customized tracking results for non TF/Pytorch workloads.
- Training jobs of experiment typically generate model artifacts (files) which need persisted, and both of notebook, model serving needs to load model artifacts from persistent storage.
- There're various of meta information, such as experiment meta, model registry, model serving, notebook, experiment, environment, etc. We need be able to read these meta information back.
- We also have code for experiment (like training/batch-prediction), notebook (ipynb), and model servings.
- And notebook/experiments/model-serving need depend on environments (dependencies such as pip, and Docker Images).

| Object Type | Characteristics | Where to store |
| --- | --- | --- |
| Metrics: tf.events | Time series data with k/v, appendable to file | Local/EBS, HDFS, Cloud Blob Storage |
| Metrics: other tracking metrics | Time series data with k/v, appendable to file | Local, HDFS, Cloud Blob Storage, Database |
| Logs | Large volumes, #files are potentially huge. | Local (temporary), HDFS (need aggregation), Cloud Blob Storage |
| Submarine Metastore | CRUD operations for small meta data. | Database |
| Model Artifacts | Size varies for model (from KBs to GBs). #files are potentially huge. | HDFS, Cloud Blob Storage |
| Code | Need version control. (Please find detailed discussions below for code storage and localization) | Tarball on HDFS/Cloud Blog Storage, or Git |
| Environment (Dependencies, Docker Image) |  | Public/private environment repo (like Conda channel), Docker registry. |

There're following ways to get experiment code:

**1) Code is part of Git repo:** (***Recommended***)

This is our recommended approach, once code is part of Git, it will be stored in version control, any change will be tracked, and much easier for users to trace back what change triggered a new bug, etc.

**2) Code is part of Docker image:**

***This is an anti-pattern and we will NOT recommend you to use it***, Docker image can be used to include ANYTHING, like dependencies, the code you will execute, or even data. But this doesn't mean you should do it. We recommend to use Docker image ONLY for libraries/dependencies.

Making code to be part of Docker image makes hard to edit code (if you want to update a value in your Python file, you will have to recreate the Docker image, push it and rerun it).

**3) Code is part of S3/HDFS/ABFS:**

User may want to store their training code to a tarball on a shared storage. Submarine need to download code from remote storage to the launched container before running the code.

To make user experiences keeps same across different environment, we will localize code to a same folder after the container is launched, preferably `/code`

For example, there's a git repo need to be synced up for an experiment/notebook/model-serving (example above):

```text
experiment: #Or notebook, model-serving 
       name: "abc", 
       environment: "team-default-ml-env" 
       ... (other fields) 
             code: 
           sync_mode: git 
           url: "https://foo.com/training-job.git"  
```

After localize, `training-job/` will be placed under `/code`

When we running on K8s environment, we can use K8s's initContainer and emptyDir to do these things for us. K8s POD spec (generated by Submarine server instead of user, user should NEVER edit K8s spec, that's too unfriendly to data-scientists):

```text
apiVersion: v1 
kind: Pod 
metadata: 
  name: experiment-abc 
spec: 
  containers: 
  - name: experiment-task 
    image: training-job 
    volumeMounts: 
    - name: code-dir 
      mountPath: /code 
  initContainers: 
  - name: git-localize 
    image: git-sync 
    command: "git clone .. /code/" 
    volumeMounts: 
    - name: code-dir 
      mountPath: /code 
  volumes: 
  - name: code-dir 
    emptyDir: {} 
```

The above K8s spec create a code-dir and mount it to `/code` to launched containers. The initContainer `git-localize` uses `https://github.com/kubernetes/git-sync` to do the sync up. (If other storages are used such as s3, we can use similar initContainer approach to download contents)

Other than ML-related objects, we have system-related objects, including:

- Daemon logs (like logs of Submarine server).
- Logs for other dependency components (like Kubernetes logs when running on K8s).
- System metrics (Physical resource usages by daemons, launched training containers, etc.).

All these information should be handled by 3rd party system, such as Grafana, Prometheus, etc. And system admins are responsible to setup these infrastructures, dashboard. Users of submarine should NOT interact with system related metrics/logs. It is system admin's responsibility.

It is possible user has needs to have an attachable volume for their experiment / notebook, this is especially useful for notebook storage, since contents of notebook can be automatically saved, and it can be used as user's home folder.

Downside of attachable volume is, it is not versioned, even notebook is mainly used for adhoc exploring tasks, an unversioned notebook file can lead to maintenance issues in the future.

Since this is a common requirement, we can consider to support attachable volumes in Submarine in a long run, but with relatively lower priority.

Describe what Submarine project should own and what Submarine project should NOT own.

---

<a id="designdocs-submarine-server-architecture"></a>

<!-- source_url: https://submarine.apache.org/docs/designDocs/submarine-server/architecture/ -->

<!-- page_index: 32 -->

# Submarine Server Implementation

Version: 0.8.0

```text
    +---------------Submarine Server ---+ 
    |                                   | 
    | +------------+ +------------+     | 
    | |Web Svc/Prxy| |Backend Svc |     |    +--Submarine Asset + 
    | +------------+ +------------+     |    |Project/Notebook  | 
    |   ^         ^                     |    |Model/Metrics     | 
    +---|---------|---------------------+    |Libraries/Dataset | 
        |         |                          +------------------+ 
        |         | 
        |      +--|-Compute Cluster 1---+    +--Image Registry--+ 
        +      |  |                     |    |   User's Images  | 
      User /   |  +                     |    |                  | 
      Admin    | User Notebook Instance |    +------------------+ 
               | Experiment Runs        | 
               +------------------------+    +-Data Storage-----+ 
                                             | S3/HDFS, etc.    | 
               +----Compute Cluster 2---+    |                  | 
                                             +------------------+ 
                        ... 
```

Here's a diagram to illustrate the Submarine's deployment.

- Submarine Server consists of web service/proxy, and backend services. They're like "control planes" of Submarine, and users will interact with these services.
- Submarine server could be a microservice architecture and can be deployed to one of the compute clusters. (see below, this will be useful when we only have one cluster).
- There're multiple compute clusters that could be used by Submarine service. For user's running notebook instance, jobs, etc. they will be placed to one of the compute clusters by user's preference or defined policies.
- Submarine's asset includes project/notebook(content)/models/metrics/dataset-meta, etc. can be stored inside Submarine's own database.
- Datasets can be stored in various locations such as S3/HDFS.
- Users can push container (such as Docker) images to a preconfigured registry in Submarine, so Submarine service can know how to pull required container images.
- Image Registry/Data-Storage, etc. are outside of Submarine server's scope and should be managed by 3rd party applications.

Submarine server is designed to allow data scientists to access notebooks, submit/manage jobs, manage models, create model training workflows, access datasets, etc.

Submarine Server exposed UI and REST API. Users can also use CLI / SDK to manage assets inside Submarine Server.

```text
           +----------+ 
           | CLI      |+---+ 
           +----------+    v              +----------------+ 
                         +--------------+ | Submarine      | 
           +----------+  | REST API     | |                | 
           | SDK      |+>|              |+>  Server        | 
           +----------+  +--------------+ |                | 
                           ^              +----------------+ 
           +----------+    | 
           | UI       |+---+ 
           +----------+ 
```

REST API will be used by the other 3 approaches. (CLI/SDK/UI)

The REST API Service handles HTTP requests and is responsible for authentication. It acts as the caller for the JobManager component.

The REST component defines the generic job spec which describes the detailed info about job. For more details, refer to [here](https://docs.google.com/document/d/1kd-5UzsHft6gV7EuZiPXeWIKJtPqVwkNlqMvy0P_pAw/edit#). (Please note that we're converting REST endpoint description from Java-based REST API to swagger definition, once that is done, we should replace the link with swagger definition spec).

```text
 
+-----------+ 
|           | 
| workbench +---+   +----------------------------------+ 
|           |   |   | +------+ +---------------------+ | 
+-----------+   |   | |      | |      +-------+      | |     +---------------------+ 
                |   | |      | |      |  K8s  |      | |     | +--------+   +----+ | 
+-----------+   |   | |      | |      +-------+      | |     | |        +-->+job1| | 
|           |   |   | |      | |      submitter      | |     | |        |   +----+ | 
|    CLI    +------>+ | REST | +---------------------+ +---->+ |operator|   +----+ | 
|           |   |   | |      | +---------------------+ |     | |        +-->+job2| | 
+-----------+   |   | |      | | +-------+ +-------+ | |     | +--------+   +----+ | 
                |   | |      | | |PlugMgr| |monitor| | |     |     K8s Cluster     | 
+-----------+   |   | |      | | +-------+ +-------+ | |     +---------------------+ 
|           |   |   | |      | |      JobManager     | | 
|    SDK    +---+   | +------+ +---------------------+ | 
|           |       +----------------------------------+ 
+-----------+ 
   client                          server 
```

We propose to split the original core module in the old layout into two modules, CLI and server as shown in FIG. The submarine-client calls the REST APIs to submit and retrieve the job info. The submarine-server provides the REST service, job management, submitting the job to cluster, and running job in different clusters through the corresponding runtime.

```text
 
   +----------------------Submarine Server--------------------------------+ 
   | +-----------------+ +------------------+ +--------------------+      | 
   | |  Experiment     | |Notebook Session  | |Environment Mgr     |      | 
   | |  Mgr            | |Mgr               | |                    |      | 
   | +-----------------+ +------------------+ +--------------------+      | 
   |                                                                      | 
   | +-----------------+ +------------------+ +--------------------+      | 
   | |  Model Registry | |Model Serving Mgr | |Compute Cluster Mgr |      | 
   | |                 | |                  | |                    |      | 
   | +-----------------+ +------------------+ +--------------------+      | 
   |                                                                      | 
   | +-----------------+ +------------------+ +--------------------+      | 
   | | DataSet Mgr     | |User/Team         | |Metadata Mgr        |      | 
   | |                 | |Permission Mgr    | |                    |      | 
   | +-----------------+ +------------------+ +--------------------+      | 
   +----------------------------------------------------------------------+ 
```

TODO

TODO

TODO

TODO

TODO

TODO

TODO

TODO

TODO

TODO: Describe what are the out-of-scope components, which should be handled and managed outside of Submarine server. Candidates are: Identity management, data storage, metastore storage, etc.

---

<a id="designdocs-submarine-server-experimentspec"></a>

<!-- source_url: https://submarine.apache.org/docs/designDocs/submarine-server/experimentSpec/ -->

<!-- page_index: 33 -->

# Generic Experiment Spec

Version: 0.8.0

As the machine learning platform, the submarine should support multiple machine learning frameworks, such as Tensorflow, Pytorch etc. But different framework has different distributed components for the training experiment. So that we designed a generic experiment spec to abstract the training experiment across different frameworks. In this way, the submarine-server can hide the complexity of underlying infrastructure differences and provide a cleaner interface to manager experiments

Considering the Tensorflow and Pytorch framework, we propose one spec which consists of library spec, submitter spec and task specs etc. Such as:

```yaml
name: "mnist" 
librarySpec: 
  name: "TensorFlow" 
  version: "2.1.0" 
  image: "apache/submarine:tf-mnist-with-summaries-1.0" 
  cmd: "python /var/tf_mnist/mnist_with_summaries.py --log_dir=/train/log --learning_rate=0.01 --batch_size=150" 
  envVars: 
    ENV_1: "ENV1" 
submitterSpec: 
  type: "k8s" 
  namespace: "submarine" 
taskSpecs: 
  Ps: 
    name: tensorflow 
    replicas: 2 
    resources: "cpu=4,memory=2048M,nvidia.com/gpu=1" 
  Worker: 
    name: tensorflow 
    replicas: 2 
    resources: "cpu=4,memory=2048M,nvidia.com/gpu=1" 
```

The library spec describes the info about machine learning framework. All the fields as below:

| field | type | optional | description |
| --- | --- | --- | --- |
| name | string | NO | Machine Learning Framework name. Only `"tensorflow"` and `"pytorch"` is supported. It doesn't matter if the value is uppercase or lowercase. |
| version | string | NO | The version of ML framework. Such as: 2.1.0 |
| image | string | NO | The public image used for each task if not specified. Such as: apache/submarine |
| cmd | string | YES | The public entry cmd for the task if not specified. |
| envVars | key/value | YES | The public env vars for the task if not specified. |

It describes the info of submitter which the user specified, such as k8s. All the fields as below:

| field | type | optional | description |
| --- | --- | --- | --- |
| type | string | NO | The submitter type, supports `k8s` now |
| configPath | string | YES | The config path of the specified resource manager. You can set it in submarine-site.xml if run submarine-server locally |
| namespace | string | NO | It's known as namespace in Kubernetes. |
| kind | string | YES | It's used for k8s submitter, supports TFJob and PyTorchJob |
| apiVersion | string | YES | It should pair with the kind, such as the TFJob's api version is `kubeflow.org/v1` |

It describes the task info, the tasks make up the experiment. So it must be specified when submit the experiment. All the tasks should putted into the key value collection. Such as:

```yaml
taskSpecs: 
  Ps: 
    name: tensorflow 
    replicas: 2 
    resources: "cpu=4,memory=2048M,nvidia.com/gpu=1" 
  Worker: 
    name: tensorflow 
    replicas: 2 
    resources: "cpu=4,memory=2048M,nvidia.com/gpu=1" 
```

All the fields as below:

| field | type | optional | description |
| --- | --- | --- | --- |
| name | string | YES | The experiment name, if not specify using the library name |
| image | string | YES | The experiment docker image |
| cmd | string | YES | The entry command for running task |
| envVars | key/value | YES | The environment variables for the task |
| resources | string | NO | The limit resource for the task. Formatter: cpu=%s,memory=%s,nvidia.com/gpu=%s |

For more info see [SUBMARINE-321](https://issues.apache.org/jira/browse/SUBMARINE-321)

---

<a id="designdocs-wip-designs-submarine-launcher"></a>

<!-- source_url: https://submarine.apache.org/docs/designDocs/wip-designs/submarine-launcher/ -->

<!-- page_index: 34 -->

# Submarine Launcher

Version: 0.8.0

> [!WARNING]
> **<a id="designdocs-wip-designs-submarine-launcher--warning"></a>

 warning**
> Please note that this design doc is working-in-progress and need more works to complete.

Submarine is built and run in Cloud Native, taking advantage of the cloud computing model.

To give full play to the advantages of cloud computing.
These applications are characterized by rapid and frequent build, release, and deployment.
Combined with the features of cloud computing, they are decoupled from the underlying hardware and operating system, and can easily meet the requirements of scalability, availability, and portability. And provide better economy.

In the enterprise data center, submarine can support k8s/docker three resource scheduling systems;
in the public cloud environment, submarine can support these cloud services in GCE/AWS/Azure;

The submarine server is a long-running services in the daemon mode.
The submarine server is mainly used by algorithm engineers to provide online front-end functions such as algorithm development, algorithm debugging, data processing, and workflow scheduling.
And submarine server also mainly used for back-end functions such as scheduling and execution of jobs, tracking of job status, and so on.

Through the ability of rolling upgrades, we can better provide system stability.
For example, we can upgrade or restart the workbench server without affecting the normal operation of submitted jobs.

You can also make full use of system resources.
For example, when the number of current developers or job tasks increases, The number of submarine server instances can be adjusted dynamically.

In addition, submarine will provide each user with a completely independent workspace container.
This workspace container has already deployed the development tools and library files commonly used by algorithm engineers including their operating environment.
Algorithm engineers can work in our prepared workspaces without any extra work.

Each user's workspace can also be run through a cloud service.

With the cluster function of submarine, each service only needs to run in the container, and it will automatically register the service in the submarine cluster center.
Submarine cluster management will automatically maintain the relationship between service and service, service and user.

![cloud-service](assets/images/multi-dc-cloud-420a103fad1e4af8a56287f083760d92_6bd005b46057b738.png)

The submarine launcher module defines the complete interface.
By using this interface, you can run the submarine server, and workspace in k8s / docker / Rancher / OpenShift / AWS / GCE / Azure.

In order to allow some small and medium-sized users without k8s to use submarine, we support running the submarine system in docker mode.

Users only need to provide several servers with docker runtime environment.
The submarine system can automatically cluster these servers into clusters, manage all the hardware resources of the cluster, and run the service or workspace container in this cluster through scheduling algorithms.

submarine operator

This section is currently described based on the Rancher Desktop.

Since we have replaced Traefik with Istio from 0.8.0, we need to turn off the Traefik in `Kubernetes Settings`.
At the same time, we need to set kubernetes version to 1.21+, the minimum CPUs to 4, and the minimum Memory to 8G.

Rancher Desktop use [Local Path Provisioner](https://github.com/rancher/local-path-provisioner) as the provisioner for StorageClass by default, so we need to modify the relevant configuration of StorageClass when using Helm to install Submarine.

```yaml
storageClass: 
  volumeBindingMode: WaitForFirstConsumer 
  provisioner: rancher.io/local-path 
```

For other installation, please refer to [Launch submarine in the cluster](https://submarine.apache.org/docs/next/gettingStarted/quickstart#launch-submarine-in-the-cluster).
In addition, we can use [kube-explorer](https://github.com/cnrancher/kube-explorer) to open Rancher Dashboard.

[TODO]

[TODO]

[TODO]

[TODO]

---

<a id="designdocs-wip-designs-security-implementation"></a>

<!-- source_url: https://submarine.apache.org/docs/designDocs/wip-designs/security-implementation/ -->

<!-- page_index: 35 -->

# Security Implementation

Version: 0.8.0

Users credential includes Kerberoes Keytabs, Docker registry credentials, Github ssh-keys, etc.

User's credential must be stored securitely, for example, via KeyCloak or K8s Secrets.

(More details TODO)

We use [pac4j](https://www.pac4j.org/) as the secure authentication component of `submarine-server`.
Based on `pac4j`, we plan to support popular authentication services such as OAuth2/OpenID Connect (OIDC), LDAP, SAML, CAS, etc.
and use a token-based method to handle external request services and internal message communication.
In the initial version we will first integrate OAuth2/OIDC, LDAP, and a simple login mode that does not rely on other authentication services.
There are already some PRs in the community to try to integrate some authentication services into `submarine`
( [New SSO function based on OIDC](https://github.com/apache/submarine/pull/833) and [Create rest api to authenticate user from LDAP](https://github.com/apache/submarine/pull/419) ), We will try to do combines on the basis of these PRs together.

When supported authentication, we will also support a way to turn off authentication and call the service directly, so that previous versions of submarine that not support authentication can call the service.
Authentication is provided by default in submarine, but we can also turn off authentication by manually setting `submarine.auth.type` to `none`.

Provides a simple way for authentication.
When users log in to the system, the username and password entered will be matched against the `sys_user` table within the system, and if the form is met a `token` will be generated and returned to the frontend.
All services will need to carry the `token` in the request header to confirm the user's identity.

```text
Authorization: Bearer <token> 
```

Supports OAuth2 as a user authentication service, requiring a jump to a third-party authentication platform for single sign-on services when logging into `submarine`.
`Submarine` requires an OAuth2 token as an authentication credential, including the refresh token.
If the logged-in user is not in `submarine`, the user data will be created automatically.

OIDC is similar to OAuth2, except that `submarine.auth.oidc.discover.uri` is required to support [OpenID Connect Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html), where an OpenID server publishes its metadata at a well-known URL, typically

```text
https://server.com/.well-known/openid-configuration 
```

This URL returns a JSON listing of the OpenID/OAuth endpoints, supported scopes and claims, public keys used to sign the tokens, and other details.
The `pac4j` can use this information to construct a request to the OpenID server.
The field names and values are defined in the OpenID Connect Discovery Specification. Here is an example of data returned:

```json
{"issuer": "https://example.com/","authorization_endpoint": "https://example.com/authorize","token_endpoint": "https://example.com/token","userinfo_endpoint": "https://example.com/userinfo","jwks_uri": "https://example.com/.well-known/jwks.json","scopes_supported": ["pets_read","pets_write","admin" ],"response_types_supported": ["code","id_token","token id_token" ],"token_endpoint_auth_methods_supported": ["client_secret_basic" ],...}
```

[TODO]

[TODO]

[TODO]

| Attribute | Description | Type | Default | Comment |
| --- | --- | --- | --- | --- |
| submarine.auth.type | Supported authentication types, currently available are: none, simple, oauth2/oidc, ldap, kerberos, saml, cas | string | none | Only one authentication method can be supported at any one time |
| submarine.auth.token.maxAge | Expiry time of the token (minute) | int | 1 day |  |
| submarine.auth.refreshToken.maxAge | Expiry time of the refresh token (minute) | int | 1 hour |  |
| submarine.cookie.http.only | HttpOnly Cookie | boolean | false |  |
| submarine.cookie.secure | Secure Cookie | boolean | false |  |
| submarine.cookie.samesite | SameSite Cookie, can be Lax, Strict, None(or empty) | string |  | <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite> |
| submarine.auth.oauth2.client.id | OAuth2 client id | string |  |  |
| submarine.auth.oauth2.client.secret | OAuth2 client secret | string |  |  |
| submarine.auth.oauth2.client.flows | OAuth2 flows, can be: authorizationCode, implicit, password or clientCredentials | string |  |  |
| submarine.auth.oauth2.scopes | The available scopes for the OAuth2 security scheme. A map between the scope name and a short description for it. | string |  |  |
| submarine.auth.oauth2.token.uri | OAuth2 access token uri | string |  |  |
| submarine.auth.oauth2.refresh.uri | OAuth2 refresh token uri | string |  |  |
| submarine.auth.oauth2.authorization.uri | OAuth2 authorization uri | string |  |  |
| submarine.auth.oauth2.logout.uri | OAuth2 logout uri | string |  |  |
| submarine.auth.oidc.client.id | OIDC client id | string |  |  |
| submarine.auth.oidc.client.secret | OIDC client Secret | string |  |  |
| submarine.auth.oidc.discover.uri | OIDC discovery uri | string |  |  |
| submarine.auth.ladp.provider.uri | LDAP provider uri | string |  |  |
| submarine.auth.ladp.baseDn | LDAP base DN | string |  | base DN is the base LDAP distinguished name for your LDAP server. For example, ou=dev,dc=xyz,dc=com |
| submarine.auth.ladp.domain | LDAP AD domain | string |  | AD domain is the domain name of the AD server. For example, corp.domain.com |

We use `javax.servlet.Filter` in the server to determine if authentication information exists for a user.
The `Filter` is implemented for each authentication type and is configured according to the implementation of the type specified by `pac4j`.
Also, a `SecurityFactory` class is provided that instantiates the specified `Filter` class into Jetty's filter based on `submarine.auth.type`.

Except in the case of `submarine.auth.type` being `none`, and some APIs necessary for authentication (login requests, etc.), we will require the token to be included in the header.
The token is generated and verified based on `pac4j` and processed inside the `Filter` class, incorrect token or no token will return a 401 HTTP code.

When a token expires, it can be regenerated by calling the refresh token method. The default token expiry time is now set to 1 day (by modifying `submarine.auth.token.maxAge`) and the refresh token expiry time is 1 hour.

Describe the design of relevant user tables, user registration/modification/deletion processes, and the processing logic associated with authenticated login
(including the mapping of attributes for automatically registered users when integrating with other authentication platforms, etc.).

We use `sys_user` table to store user information for submarines.
When `submarine.auth.type` is `simple`, the user's login operation will match `user_name` and `password` (encrypted) in `sys_user`. Only when the user name and password match will the login succeed.
When `submarine.auth.type` is `ldap`, the user's login will operation request the LDAP and verify that the username and password are correct. A new record will be added to the `sys_user` table if the logged-in user does not exist.
When logging in using other third-party authentication (OAuth2/OpenID Connect (OIDC), SAML, CAS etc.), the login page will automatically jump to the third-party service and revert back to the submarine after a successful login. A new record will be added to the `sys_user` table if the logged-in user does not exist.

[TODO]

[TODO]

[TODO]

---
