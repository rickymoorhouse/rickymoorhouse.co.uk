---
author: rickymoorhouse
comments: true
date: 2015-12-12 08:40:57+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2015/12/12/automatically-publish-your-api-when-you-push-to-github/
slug: automatically-publish-your-api-when-you-push-to-github
title: Automatically publish your API when you push to github
---

*Updated 11th October 2016 for API Connect*

In less than half an hour I could update my project to automatically publish my API in IBM API Connect - Here's the steps...

Sign up for  [API Connect](https://console.ng.bluemix.net/catalog/services/api-connect/) through Bluemix by creating an API Connect service instance - if you don't already have a Bluemix account you can sign up for a free trial account.

Install and configure the new toolkit CLI - replacing eu with au or us if you chose a different bluemix region:

```bash
npm install -g apiconnect 
apic config:set server=eu.apiconnect.ibmcloud.com
apic login
```



Create a product definition for your API:


​    
```bash
apic create --type product --title "Travel Information" --apis product.yaml
```



Adjust the product definition as needed in your favourite editor

Add the x-ibm-configuration extensions to your swagger document to configure what happens when someone calls the API - in my case invoke the backend API


​    
```yaml
x-ibm-configuration:
  enforced: true
  phase: realized
  testable: true
  cors:
    enabled: true
  assembly:
    execute:
      - invoke:
          title: invoke
          target-url: '<backend url>'
```



Now switch over to your CodeShip account, load your project and go to the Deployment section of your project.

Add a custom script option and confiigure the following script (adding your details as needed):


​    
```bash
npm install -g apiconnect
apic config:set server=eu.apiconnect.ibmcloud.com
apic login -u <username> -p <password>
apic config:set organization=<org>
apic push docs/swagger.yaml
apic stage --catalog=sb docs/travel-information.yaml
apic publish --catalog=sb docs/travel-information.yaml</code>
```



Commit and push to your repository and your updated API will be pushed to API Management! - [Here is my example API](https://developer.beta.apim.ibmcloud.com/hirickymoorhousecouk/sb)

If you don't already have a CodeShip account you can [sign up to CodeShip](https://codeship.com/registrations/new) with your github account and create link in your github repository. You can then set up the tests and deployment steps in the project settings.
