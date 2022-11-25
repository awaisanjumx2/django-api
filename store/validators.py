from django.core.exceptions import ValidationError


def validate_file_size(file):
    max_file_size = 100
    if file.size > max_file_size * 1024:
        raise ValidationError(
            f'File size should not be greater than {max_file_size} KB')
