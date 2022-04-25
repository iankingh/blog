---
title: "AngularCheatSheet"
date: 2020-11-06T22:11:38+08:00
draft: true
categories:
 - "筆記"
tags:
 - "Angular"
 - "FrontEnd"
toc: true
---

## Angular Cheat Sheet (Angular 小抄)
<!--more-->

## Angular CLI(Angular 指令)

- `npm install -g @angular/cli` :
This command will install the Angular CLI into our local machine using npm.(此命令將使用npm將Angular CLI安裝到我們的本地計算機中。)
- `ng new <application name>` : This will setup a new Angular application using the ng new command.(這將使用ng new命令設置一個新的Angular應用程序。)
- `ng new --help`: This returns all available Angular command list.(這將返回所有可用的Angular命令列表)

- `ng generate component <name>`: This will create a new component on our application. We can also use the `ng g c <name>` shorthand to do this.(這將在我們的應用程序上創建一個新組件。我們也可以使用ng g c <name>的簡寫方式來做到這一點。)

- `ng build`: Builds the application for production and stores it in the `dist` directory.

- `ng serve -o`: Serves the application by opening up the application in a browser using any port 4200 or any available port. `-o` : open



- `ng g d <directive name>`: This command angular directive.
- `ng g s <service name>` : Creates a new Javascript class based service.
- `ng g p <pipe name>`: Generates a new pipe
- `ng g cl <destination>` : This will create a new class in the specified directory.
- 



## Angular Lifecycle Hooks

A component in Angular has a life-cycle, a number of different phases it goes through from birth to death.We can hook into those different phases to get some pretty fine grained control of our application.Here are some of the hooks:

- `ngOnChanges`: This is called whenever one of input properties change.
- `ngOnInit`: This is called immediately after `ngOnChanges` is completed and it is called once.
- `ngOnDestroy`: Called before angular destroys a directory or component
- `ngDoCheck`: Whenever a change detection is ran, this is called.
- `ngAfterContentInit`: Invoked *after* Angular performs any content projection into the component’s view.
- `ngAfterContentChecked`:This is called each time the content of the given component has been checked by the change detection mechanism of Angular.
- `ngAfterViewInit` This is called when the component’s view has been fully initialized.
- `ngAfterViewChecked`: Invoked each time the view of the given component has been checked by the change detection mechanism of Angular.

## How Angular Hooks are used

Always remember that hooks working in a component or directory, so use them in our component, we can do this:

```
`class ComponentName {
    @Input('data') data: Data;
    constructor() {
        console.log(`new - data is ${this.data}`);
    }
    ngOnChanges() {
        console.log(`ngOnChanges - data is ${this.data}`);
    }
    ngOnInit() {
        console.log(`ngOnInit  - data is ${this.data}`);
    }
    ngDoCheck() {
        console.log("ngDoCheck")
    }
    ngAfterContentInit() {
        console.log("ngAfterContentInit");
    }
    ngAfterContentChecked() {
        console.log("ngAfterContentChecked");
    }
    ngAfterViewInit() {
        console.log("ngAfterViewInit");
    }
    ngAfterViewChecked() {
        console.log("ngAfterViewChecked");
    }
    ngOnDestroy() {
        console.log("ngOnDestroy");
    }
}
```



## Component DOM

Angular comes with its DOM features where you can do a whole lot from binding of data and defining of dynamic styles. Let’s take a look at some features:
Before we dive into the features, a simple component.ts file is in this manner:

```
import { Component } from '@angular/core';
@Component({
    // component attributes
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.less']
})
export class AppComponent {
    name: 'Sunil';
}
```



## Lets look at some template syntax:

- `Interpolation`: using ```{{data to be displayed}}``` will display dynamic content from the ts file.
- `<button (click)="callMethod()" ... />` : Adding Click events to buttons to call a method defined in the ts file
- `<button *ngIf="loading" ... />`: Adding Conditionals to to elements. Conditionals have to listen to truthy or falsy value.
- `*ngFor="let item of items``"`: iterate throught a defined list of items.Picture this as a for loop.
- `<div [ngClass]="{green: isTrue(), bold: itTrue()}"/>`: Adding dynamic classes based on conditionals.
- `<div [ngStyle]="{'color': isTrue() ? '#bbb' : '#ccc'}"/>`: Adding dynamic styles to template based on conditions

## Component Communication

Passing data from one component to another can be a little bit tricky in Angular. You can pass data from child to parent, parent to parent and between two unrelated components:

- `input()`: This method helps To pass value into child component.

``export class SampleComponent {@Input() value: 'Some Data should go in here';}``
Child components are registered in parents component like this:

```
<child-component [value]="data"></child-component>
```



- `output()`: This method Emits event to the parent component. Bunch of data can be passed into emitted event which makes it a medium of passing data from child to parent:

To Emit the event from the child component:

```
@Output() myEvent: EventEmitter < MyModel > = new EventEmitter();
calledEvt(item: MyModel) {
    this.myEvent.emit(item);
}
```



And then the parent component listens to that event:

```
<parent-component 
(myEvent)="callMethod()"></parent-component>
```



## Angular Routing

Routing is another cool feature of Angular, with the Angular Routing system we can navigate through pages and even add route guards.

- Component Routing: We can define routes in our application by defining the path and the component to be rendered: `` const routes: Routes = [ { path: 'home', component:HomeComponent }, { path: 'blog/:id', component: BlogPostCompoent }, { path: '**', component: PageNotFoundComponent } ]; ``

For routing to work, add this the your `angular.module.ts` file:

```
RouterModule.forRoot(routes)
```



There are situations where by you want to keep track of what is happening in your routes, you can add this to enable tracking in your angular project:

```
RouterModule.forRoot(routes,{enableTracking:true})
```



To navigate through pages in Angular, we can use the `routerLink` attribute which takes in the name of the component we are routing to:

```
<a routerLink="/home" routerLinkActive="active"> Crisis Center</a>
```



The `routerLinkActive="active``"` will add an active class to the link when active.

## Writing Route Guards

We can define guard for route authentication. We can use the `CanActivate` class to do this:

```
class AlwaysAuthGuard implements CanActivate {        
        canActivate() {
                return true;
        }
}
```



To use this rote guard in our routes we can define it here:

```
const routes: Routes = [
  { path: 'home', component:HomeComponent },
  { path: 'blog/:id', component: BlogPostCompoent,canActivate: [AlwaysAuthGuard],  },
    { path: '**', component: PageNotFoundComponent }
];
```



## Angular Services

Angular services comes in handy when you can to do things like handling of http request and seeding of data on your application.They focus on presenting data and delegate data access to a service.

```
@Injectable()
export class MyService {
    public users: Users[];
    constructor() { }
    getAllUsers() {
        // some implementation
    }
}
```



To use this service in your component, import it using the import statement and then register it in the constructor

```
import MyService from '<path>'
constructor(private UserService: MyService) 
```



To make things easier, we can use this command to generate a service in Angular

```
ng g s <service name>
```



## Http Service

Angular comes with its own http service for making http request. To use it, you have to first of all import it into your root module:

```
import { HttpClientModule} from "@angular/common/http";
```



After importing it, we can now use it inside our service for making of http request:

```
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
    providedIn: 'root'
})
export class UserService {
    constructor(private http: HttpClient) { }
    getAllUsers() {
        return this.http.get(`${baseURL}admin/list-users`);
    }
}
```



## Http Interceptors

An **interceptor** is a piece of code that gets activated for every single **HTTP** request received by your application. Picture an interceptor as a middleware in nodejs where by where http request made is passed through this piece of code.

To define an interceptor create a `http-interceptor.ts` file inside your src directory and add this:

```
import { Injectable } from '@angular/core';
import {
    HttpEvent,
    HttpInterceptor,
    HttpHandler,
    HttpRequest,
    HttpErrorResponse,
    HttpResponse
} from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';
@Injectable({
    providedIn: 'root'
})
export class HttpConfigInterceptor implements HttpInterceptor {
    constructor() { }
    intercept(req: HttpRequest<any>, next: HttpHandler) {
        // Get the auth token from  localstorage.
        const authToken = localStorage.getItem('token');
        // Clone the request and replace the original headers with
        // cloned headers, updated with the authorization.
        const authReq = req.clone({
            headers: req.headers.set('Authorization', authToken)
        });
        // send cloned request with header to the next handler.
        return next.handle(authReq);
    }
}
```



This is a simple interceptor which checks if users has token in their device localstorage. If the user does , it will pass the token in all the http headers.

## Pipes

Pipes in Angular gives us the ability to transform data to any specific format. For example you can write a simple pipe that will format an integer to a currency format or format dates to any form.
Angular comes with some built in pipes like the date and currency pipe.

We can define our own custom pipes too by doing this:

```
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({ name: 'exponentialStrength' })
export class ExponentialStrengthPipe implements PipeTransform {
    transform(value: number, exponent?: number): number {
        return Math.pow(value, isNaN(exponent) ? 1 : exponent);
    }
}
```



to use a pipe in our component we can do this:
\```{{power | exponentialStrength: factor}}`


## 參考

Angular Cheat Sheet - DEV

https://dev.to/suniljoshi19/angular-cheat-sheet-46bo?fbclid=IwAR1hL9OTHVIthSFCqOH4pGuMK3447-ru5vPxKT-EI4AAOyGoLAJ3iiQ7K8I