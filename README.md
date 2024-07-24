# Streamlit samples on Azure App Services
Streamlit applications are a really fast way of creating simple data-driven web applications, so a especially valuable for proof of concepts.

Streamlit is a little tricky to configure correctly on Azure App Services (web apps), so this repo has a couple of sample Streamlit apps.

1. A simple Streamlit application
2. An OpenAI chat application built on Streamlit which uses an Azure OpenAI service.

![alt text](./streamlit-chat-app-services.png "Streamlit chat App Service")

This has been forked from https://github.com/benalexkeen/streamlit-azure-app-services

# Deployment

The deployment below, creates the Azure OpenAI chat example using an App Services startup command to ensure the App Service runtime plays well with Streamlit.

```
python -m streamlit run app/openai-chat.py --server.port 8000 --server.address 0.0.0.0"
```

[![Deploy To Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fjometzg%2Fstreamlit-azure-app-services%2Fmain%2Fazuredeploy.json)

You will need to provide some settings from an existing Azure OpenAI instance. These get put the *Environment variables* section of the web app. These are to connect the app to the correct Azure OpenAI service instance.

![alt text](./app-service-streamlit-openai-settings.png "App Service Environment Variables")
