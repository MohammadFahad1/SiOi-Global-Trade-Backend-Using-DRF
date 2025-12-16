from django.core.exceptions import ValidationError

def validate_file_size(file):
    max_size_mb = 5
    max_size_bytes = max_size_mb * 1024 * 1024
    if file.size > max_size_bytes:
        raise ValidationError(f"File size cannot exceed {max_size_mb} MB.")
