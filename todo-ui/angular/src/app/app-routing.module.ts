import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {RouterModule, Routes} from "@angular/router";
import {PageNotFoundComponent} from "./page-not-found/page-not-found.component";
import {TaskComponent} from "./task/task.component";
import {ListComponent} from "./list/list.component";

const routes: Routes = [
    {
        path: '',
        pathMatch: 'full',
        component: ListComponent
    },
    {
        path: 'task',
        pathMatch: 'full',
        component: TaskComponent
    },
    {
        path: '**',
        component: PageNotFoundComponent
    }
];

@NgModule({
  declarations: [],
  imports: [
    RouterModule.forRoot(routes),
    CommonModule
  ]
})
export class AppRoutingModule { }
