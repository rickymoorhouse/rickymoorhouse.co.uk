---
author: rickymoorhouse
comments: true
date: 2015-12-12 08:40:57+00:00
layout: post
link: http://blog.rickymoorhouse.co.uk/2015/12/12/automatically-publish-your-api-when-you-push-to-github/
slug: automatically-publish-your-api-when-you-push-to-github
title: Automatically publish your API when you push to github
wordpress_id: 8248
---

In less than half an hour I could update my project to automatically publish my API in the new IBM API Management beta - Here's the steps...

Sign up for the [new API Management beta](http://ibm.biz/apimbeta/), just click through to 'Cloud' and login with your IBMID (If you don't have one you can [create one](https://www.ibm.com/account/profile/us?page=reg)) and once you've accepted the terms and conditions your organisation will be created.

Install and configure the new toolkit CLI:


    
    <code class=" language-none">npm install -g https://beta.apim.ibmcloud.com/apimanager/toolkit/apim.toolkit
    apim config:set server=beta.apim.ibmcloud.com
    apim login</code>



Create a product definition for your API:


    
    <code>apim create --type product --title "Travel Information" --apis product.yaml</code>



Adjust the product definition as needed in your favourite editor

Add the x-ibm-configuration extensions to your swagger document to configure what happens when someone calls the API - in my case invoke the backend API


    
    <code class=" language-none">x-ibm-configuration:
      enforced: true
      phase: realized
      testable: true
      cors:
        enabled: true
      assembly:
        execute:
          - invoke:
              title: invoke
              target-url: '<backend url>'</code>



Now switch over to your CodeShip account, load your project and go to the Deployment section of your project.

Add a custom script option and confiigure the following script (adding your details as needed):


    
    <code class=" language-none">npm install -g https://beta.apim.ibmcloud.com/apimanager/toolkit/apim.toolkit
    apim config:set server=beta.apim.ibmcloud.com
    apim login -u <username> -p <password>
    apim config:set organization=<org>
    apim push docs/swagger.yaml
    apim stage --catalog=sb docs/travel-information.yaml
    apim publish --catalog=sb docs/travel-information.yaml</code>



Commit and push to your repository and your updated API will be pushed to API Management! - [Here is my example API](https://developer.beta.apim.ibmcloud.com/hirickymoorhousecouk/sb)

If you don't already have a CodeShip account you can [sign up to CodeShip](https://codeship.com/registrations/new) with your github account and create link in your github repository. You can then set up the tests and deployment steps in the project settings.
