# Django FullStack Project

Table Of Content

- [Overview](#overview)
- [Design](#design)
    - [UX](#ux)
        - [Personas & user stories](#personas--users-stories)
        - [Information Architecture](#information-architecture)
        - [Wireframes](#wireframes)
    - [Database](#database)
- [Workflow](#workflow)
    - [Story Map](#story-map)
- [Tech used](#tech-used)


# Overview

This E-commerce project allows users to purchase 3D printed design products (miniatures, gadgets, small home and office 
accessories, etc.).
While the 3D printing service is clearly out of this project's scope, it handles all the functionality of an e-commerce app: 
browsing through design products and categories, users authentication, payment and users customized interaction with the platform.

The platform has two main types of users:
- Customers, purchasing design products in the store.  
- Partners, selling their designs and purchasing any products in the store.  

Customers have the possibility to choose the material and color for each product they purchase. They can keep track of 
their orders, rate and comment after payment and subscribe for email alerts for delivery status.  
Partners can, additionally, upload their designs and choose materials and colors that will be available to the customers. 
They may edit these choices, upload a new design version or remove it from the store. They can subscribe for email alerts when a product 
is sold, when a customer rates or comments one of their designs.  


# Design

## UX

All UX preliminary work can be found in [ux_documentation](./ux_documentation).

### Personas & Users stories

[Personas and user stories](./ux_documentation/persona_user_stories.md) are detailed in separate file in the ux documentation 
directory.

### Information Architecture

The very first step prior working on any wireframe is to set the [zoning](./ux_documentation/zoning.jpg).

- All user centric features are accessible from the user icon in navbar once logged in. The navbar displays all 
session related infos (cart, etc.).  
- All app core features (browsing, product categories, blog, etc.) are accessible from the side menu.  
- All legal information and platform support is located in the footer.  

Such compartmentalization improves the first-time learning experience and prevents 
neither menus to become overloaded with links and information.  

A sub-nav zone as a navigation feedback may be added to compensate mobile visibility on nested subtree 
categories. This can become critical with bad network throttling or on a slow device. While this is less necessary on larger 
screens I've decided I would keep it for visual consistency (for now).  

The content area is divided in two zones, main content and a search field present in all browsing pages so the users can 
adjust their keyword search with fewer interaction.  


### Wireframes

I've designed the wireframes in an iterative process going through all user stories based on their priority. This approach 
helps creating an efficient features and information architecture by adding the bare minimum and making any necessary 
adjustments in respect of different users needs.  
The [user stories wireframes](./ux_documentation/user_stories_wireframes.pdf) shows the results on the persona 'priority device'
 (device the user is more likely to connect with).


## Database

Here is a draft of the [Database Relationship Diagram](./ux_documentation/shapers_db_design.png).


# Workflow

## Story Map

I have grouped user stories in this [Story Map](./ux_documentation/shapers_storymap.pdf) following the MoSCoW method
before creating the backlog and organize sprints in [ORA](https://ora.pm/) using Agile Estimation technique.  

With Tom being the main persona grouping all core features, I’ve planned a "pre-release" version (actual true 
MVP: sprint3).  
This pre-release version may not last long against competitors but the concept of pre-release is to hold stake-holder’s breath 
a bit longer (as well as customers in case of pre-launch marketing campaign) should the development be severely delayed.  


# Tech used

## Back-end

- [Python 3.8](https://docs.python.org/3.8/whatsnew/3.8.html)
- [Django 3.1](https://docs.djangoproject.com/en/3.1/)

## Front-end

- Styling is written in [SCSS](https://sass-lang.com).
- [Bootstrap4](https://getbootstrap.com/) to set up our basic template layout.
- [jQuery](https://jquery.com/) library is used for DOM manipulation and is required for Bootstrap.