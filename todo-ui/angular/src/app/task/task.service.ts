import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Task} from "../task/task.model";
import {API_URL} from "../../environments/environment.prod";

@Injectable()
export class TaskService {

    constructor(private http: HttpClient) {
    }

    public editTask(task: Task) {
        return this.http.post<Task[]>(API_URL + '/edit/' + task.id, task);
    }

    public newTask(task: Task) {
        return this.http.post<Task[]>(API_URL + '/new', task);
    }

    public deleteTask(task: Task) {
        return this.http.delete<Task[]>(API_URL + '/delete/' + task.id);
    }
}
