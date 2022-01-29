import {Component, OnInit} from '@angular/core';
import {Task} from "./task/task.model";
import {ListService} from "./list/list.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'angular';


  constructor() {

  }

}
