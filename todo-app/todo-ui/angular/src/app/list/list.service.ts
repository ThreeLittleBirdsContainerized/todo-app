import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Task} from "../task/task.model";
import {API_URL} from "../../environments/environment.prod";

@Injectable()
export class ListService {

    constructor(private http: HttpClient) {
    }

    public getAllTasks() {
        return this.http.get<Task[]>(API_URL + '/tasks');
    }
}
