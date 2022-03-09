```

 Probe           Fails
Startup ==> it won't move pod to running state
The kubelet uses startup probes to know when a container application has started. 
If such a probe is configured, it disables liveness and readiness checks until it succeeds, making sure those probes don't interfere with the application startup. 


liveness -> it will restart the container 
The kubelet uses liveness probes to know when to restart a container.

indicating that the liveness probes have failed, and the containers have been killed and recreated.

readiness -> it will move pod outof traffic
The kubelet uses readiness probes to know when a container is ready to start accepting traffic.When a Pod is not ready, it is removed from Service load balancers.
A pod with containers reporting that they are not success readinessprobe does not receive traffic through Kubernetes Services.


```
