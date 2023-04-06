# Burp Suite Target

> Vidath Dissanayake | Sri Lanka

The Target [module](../modules.md) fo [Burp Suite](../../Burp%20Suite.md).

## Sitemap

Site map allows us to map out the apps we are targeting in a tree structure. 

Every page that we visit will show up here, allowing us to automatically generate a site map for the target simply by browsing around the web app. 

[Burp Suite Professional Edition](../../editions.md#Burp%20Suite%20Professional%20Edition) would also allow us to spider the targets automatically (i.e. look through every page for links and use them to map out as much of the site as-is publicly accessible using the links between pages); however, with [Burp Suite Community Edition](../../editions.md#Burp%20Suite%20Community%20Edition), we can still use this to accumulate data whilst we perform our initial enumeration steps. 

The Site map can be especially useful if we want to map out an API, as whenever we visit a page, any API endpoints that the page retrieves data from whilst loading will show up here.


## Scope

The Scope sub-tab allows us to control what we are targeting by either including or excluding domains/IPs.


## Issue Definitions

The Issue Definitions section gives us a huge list of web vulnerabilities (complete with descriptions and references) which we can draw from should we need citations for a report or help describing a vulnerability.