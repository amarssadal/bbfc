from flask import url_for, redirect
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import ImageUploadField
from flask_login import current_user

from instance.default import IMAGE_BASE_PATH


class AdminModelView(ModelView):
    form_overrides = {'image': ImageUploadField}
    form_args = {
        'image': {
            'base_path': IMAGE_BASE_PATH,
        }
    }

    def is_accessible(self):
        return current_user.is_active and current_user.is_authenticated

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('security.login'))

