### Helm chart installation
Run the following command to install helm chart:
```
helm install --namespace todo-app todo ./todo-app-chart
```

If you want to just build the templates without running a release instance, run the following command:
```
helm install --debug --dry-run --namespace todo-app todo ./todo-app-chart
```