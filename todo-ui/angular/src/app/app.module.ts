import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { TaskComponent } from './task/task.component';
import {HttpClientModule} from "@angular/common/http";
import {ListService} from "./list/list.service";
import { ListComponent } from './list/list.component';
import {FormsModule} from "@angular/forms";
import {TaskService} from "./task/task.service";

@NgModule({
  declarations: [
    AppComponent,
    PageNotFoundComponent,
    TaskComponent,
    ListComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    RouterModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [ListService, TaskService],
  bootstrap: [AppComponent]
})
export class AppModule { }
