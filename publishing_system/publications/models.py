from django.db import models
from accounts.models import Author, Reviewer

class Publication(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    file = models.FileField(upload_to="articles/")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("submitted", "Submitted"),
        ("under_review", "Under Review"),
        ("revision_required", "Revision Required"),
        ("under_revision", "Under Revision"),
        ("accepted", "Accepted"),
        ("publishing", "Publishing"),
        ("indexed", "Indexed"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")

    def __str__(self):
        return f"{self.title} ({self.status})"


class PublicationReviewer(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="reviewers")
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reviewer.user.username} reviewing {self.publication.title}"


class Revision(models.Model):
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="revisions")
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    comments = models.TextField()
    deadline = models.DateField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    REVISION_STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("accepted", "Accepted"),
    ]
    status = models.CharField(max_length=20, choices=REVISION_STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"Revision {self.id} for {self.publication.title}"
