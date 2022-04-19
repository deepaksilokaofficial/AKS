# Integrating Docker image with ACI 

## Steps
1. Create Dockerfile consisting of commands which we want to execute.                                                                                                                                           <p></p>
2. create docker image of Dockerfile using below command.
   ```sh
     docker build -t model_demo .
   ``` 
3. Now before creating aks cluster, we have to push our image into azure container registry.
   So for that create azure container registry resource either from portal or cli.                                                                                           <p></p>
4. Go to Azure Container Registry >> Select the registry which we created >> access keys >> `enable` admin user.                                                                       <p></p>
5. Now go to CLI and login into Azure ACR (username and password is visible on access keys page).
   ```sh 
    docker login <login server>
    ```
   
6. Now tag the image .
   ```sh
    docker tag model_demo <login server>/model_demo
   ```
   
7. Push the image to ACR.
   ```sh
    docker push <login server>/model_demo
   ```
  
8. Create AKS cluster.
   ```sh
     az aks create --resource-group <name of resource group> --name myaks --generate-ssh-keys
   ```
   
9. Install kubectl (if not installed)
   ```sh
     az aks install-cli
   ```   
10. Get the AKS cluster credential.
    ```sh
    az aks get-credentials --resource-group <name of resource group> -n myaks
    ```
11. Create a Secret to hold the registry credentials.
    ```sh
      kubectl create secret docker-registry [NAME] --docker-server=<login server> --docker-username=<username> --docker-password=<password> --docker-email=<mail-id>
    ```
    * we can get the required username and password from acr.
      <p></p>
      
12. Create kubernetes deployment and service defination file(my_aks.yml)
       <p></p>    
13. Deploy the service.
    ```sh
      kubectl apply -f my_aks.yml
    ```
14. Now get the ip address to test the service.
    ```sh
    kubectl get service/model-demo
    ```
15. Final step, get the predictions.
    ```sh
     curl -i -H "Content-Type:application/json" -X POST -d{"Time":5} ip_address_of_container:5000/pred
    ```
    we can pass the feature names and values as key:value pair
    
    
 
