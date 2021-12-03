import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_get_course(api_client, course_factory):
    courses = course_factory(_quantity=1)[0]
    url = reverse('courses-detail', args=[courses.id])
    resp = api_client.get(url)
    resp_json = resp.json()
    assert resp.status_code == 200
    assert courses.id == resp_json['id']


@pytest.mark.django_db
def test_courses_list(api_client, course_factory):
    courses = course_factory(_quantity=3)
    url = reverse('courses-list')
    resp = api_client.get(url)
    resp_json = resp.json()
    assert resp.status_code == 200
    assert len(courses) == len(resp_json)


@pytest.mark.django_db
def test_courses_id_filter(api_client, course_factory):
    courses = course_factory(_quantity=3)[1]
    url = reverse('courses-list')
    resp = api_client.get(url, {'id': courses.id})
    resp_json = resp.json()[0]
    assert resp.status_code == 200
    assert courses.id == resp_json.get('id')


@pytest.mark.django_db
def test_courses_name_filter(api_client, course_factory):
    courses = course_factory(_quantity=5)[4]
    url = reverse("courses-list")
    resp = api_client.get(url, {'name': courses.name})
    resp_json = resp.json()[0]
    assert resp.status_code == 200
    assert courses.name == resp_json['name']


@pytest.mark.django_db
def test_course_create(api_client):
    url = reverse("courses-list")
    resp = api_client.post(url, {'name': 'Django-23'})
    assert resp.status_code == 201
    assert resp.data['name'] == 'Django-23'


@pytest.mark.django_db
def test_course_update(api_client, course_factory):
    courses = course_factory(_quantity=1)
    url = reverse('courses-detail', args=[courses[0].id])
    resp = api_client.patch(url, {'name': 'Java-26'})
    assert resp.status_code == 200
    assert resp.data['name'] == 'Java-26'


@pytest.mark.django_db
def test_course_delete(api_client, course_factory):
    course = course_factory(_quantity=1)
    url = reverse('courses-detail', args=[course[0].id])
    resp = api_client.delete(url)
    assert resp.status_code == 204

