export class Task {
  id: number | null;
  title: string | null;
  description: string | null;

  constructor(task: Task) {
    this.id = task.id;
    this.title = task.title;
    this.description = task.description;
  }
}
