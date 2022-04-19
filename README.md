# Integrating Docker image with ACI 

## Steps
1. Create Dockerfile consisting of commands which we want to execute.                                                                                                                                           <p></p>
2. create docker image of Dockerfile using below command.
   ```sh
     docker build -t model_demo .
   ```
  
3. login into azure.
   ```sh
     docker login azure
   ```
   
4. Create an ACI context
   ```sh
     docker context create aci myaci
   ```
   
5. Now before running our docker image on aci , we have to push our image into azure container registry.
   So for that create azure container registry resource either from portal or cli.                                                                                           <p></p>
6. Go to Azure Container Registry >> Select the registry which we created >> access keys >> `enable` admin user.                                                                       <p></p>
7. Now go to CLI and login into Azure ACR (username and password is visible on access keys page).
   ```sh 
    docker login <login server>
    ```
   
8. Now tag the image .
   ```sh
    docker tag model_demo <login server>/model_demo
   ```
   
9. Push the image to ACR.
   ```sh
    docker push <login server>/model_demo
   ```
  
10. Now create an ACI, on top of aci docker container will be running.
    ```sh
     docker --context myaci run -p 5000:5000 <login server>/model_demo
    ```
    
11. Final step, get the predictions.
    ```sh
     curl -i -H "Content-Type:application/json" -X POST -d{"Time":5} ip_address_of_container:5000/pred
    ```
    we can pass the feature names and values as key:value pair
    and IP address can be obtained from ACI overview page.
    
 
