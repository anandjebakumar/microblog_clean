from application import create_app
import os

app = create_app(config_file='config.Config')

watch_files = []
template_dir = 'application/templates'
for html_file in os.listdir(template_dir):
    watch_files.append(os.path.join(template_dir,html_file))

if __name__ == '__main__':
    app.run(debug=True,extra_files=watch_files)
