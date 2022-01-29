import {Component, OnInit} from '@angular/core';
import {Task} from "../task/task.model";
import {ListService} from "./list.service";

@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css']
})
export class ListComponent implements OnInit {

  todo: Task[] = [];
  newTaskURL: string = '';

  constructor(private listService: ListService) {

  }
  ngOnInit(): void {
    this.getTasks();
  }

  getTasks() {
    this.listService.getAllTasks().subscribe(
      data => { this.todo = data }
    )
  }

}
