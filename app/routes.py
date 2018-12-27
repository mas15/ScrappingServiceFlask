from app import app


@app.route("/status/<task_id>")
def check_status(self, task_id):
    pass
    # status = self.tasks.get(task_id)
    # if status is None:
    #     raise NotFoundError('There is no such a task')
    # return status