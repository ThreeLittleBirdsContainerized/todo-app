import {Component, Input, OnInit} from '@angular/core';
import {Task} from "./task.model";
import {ActivatedRoute, Router} from "@angular/router";
import {TaskService} from "./task.service";

@Component({
  selector: 'app-task',
  templateUrl: './task.component.html',
  styleUrls: ['./task.component.css']
})
export class TaskComponent implements OnInit {

  tasks: Task[] = [];

  currentTask: Task = {
    id: null,
    title: null,
    description: null
  };

  mode: 'edit' | 'new' = 'new';

  constructor(private router: Router, private route: ActivatedRoute, private taskService: TaskService) {
    const currentTask = this.route.snapshot.params as Task;
    if (currentTask.id) {
      this.mode = 'edit';
      this.currentTask.id = currentTask.id;
      this.currentTask.description = currentTask.description;
      this.currentTask.title = currentTask.title;
    } else {
      this.mode = 'new';
      this.currentTask = {
        id: null,
        title: null,
        description: null
      };
    }
  }

  ngOnInit(): void {
  }

  deleteTask() {
    this.taskService.deleteTask(this.currentTask).subscribe(
      data => { console.log(data); this.router.navigate(['/']); }
    )
  }

  submit() {
    if (this.mode === 'edit') {
      this.taskService.editTask(this.currentTask).subscribe(
      data => { console.log(data); this.router.navigate(['/']); }
    )
    } else if (this.mode === 'new') {
      this.taskService.newTask(this.currentTask).subscribe(
      data => { console.log(data); this.router.navigate(['/']); }
    )
    }
  }
}
