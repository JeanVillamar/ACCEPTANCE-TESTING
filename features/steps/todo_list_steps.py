import io
from contextlib import redirect_stdout
import todo_list
from behave import *

@given('the task list is empty')
def step_impl(context):
  todo_list.tasks = []

@when('I add the task "{task}"')
def step_impl(context, task):
  todo_list.add_task(task)

@then('the task list should contain {count:d} task')
def step_impl(context, count):
  assert len(todo_list.tasks) == count

@given('the task list contains')
def step_impl(context):
  for row in context.table:
    todo_list.add_task(row[0])

@when('I list the tasks')
def step_impl(context):
  output = io.StringIO()
  with redirect_stdout(output):
    todo_list.list_tasks()
  context.output = output.getvalue()

@then('it should show')
def step_impl(context):
  output = context.output.split('\n')
  tasks = todo_list.tasks
  for i in range(len(tasks)):
    row = output[i]
    description = row.split('. ')[1].split(' - ')[0]
    status = 'Completed' if tasks[i]['completed'] else 'Incomplete'
    assert description == tasks[i]['description']
    assert status in row

@when('I mark task {index:d} as completed')
def step_impl(context, index):
  todo_list.mark_completed(index)

@then('task {index:d} should appear as completed')
def step_impl(context, index):
  assert todo_list.tasks[index-1]['completed'] == True

@when('I edit task {index:d} to "{text}"')
def step_impl(context, index, text):
  todo_list.edit_task(index, text)

@then('task {index:d} should say "{text}"')
def step_impl(context, index, text):
  assert todo_list.tasks[index-1]['description'] == text

@when('I clear the task list')
def step_impl(context):
  todo_list.clear_tasks()

@then('the task list should be empty')
def step_impl(context):
  assert len(todo_list.tasks) == 0