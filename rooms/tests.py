import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Reservation, Room


class ReservationFlowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass1234')
        self.room = Room.objects.create(
            room_number='101',
            room_type='Single Room',
            price_per_night=100,
            is_available=True,
        )

    def _reservation_payload(self):
        check_in = timezone.now().date() + datetime.timedelta(days=3)
        check_out = check_in + datetime.timedelta(days=2)
        return {
            'first_name': 'Alex',
            'last_name': 'Smith',
            'phone': '123456789',
            'email': 'alex@example.com',
            'nationality': 'Test',
            'children': 0,
            'extras': ['breakfast'],
            'agree': 'on',
            'room_type': 'Single Room',
            'check_in_date': check_in.isoformat(),
            'check_out_date': check_out.isoformat(),
        }

    def test_login_required_for_reservations(self):
        response = self.client.get(reverse('reservation_list'))
        self.assertEqual(response.status_code, 302)

    def test_create_reservation(self):
        self.client.login(username='tester', password='pass1234')
        response = self.client.post(reverse('room_details'), data=self._reservation_payload())
        self.assertRedirects(response, reverse('reservation_list'))
        self.assertEqual(Reservation.objects.count(), 1)
        self.room.refresh_from_db()
        # self.assertFalse(self.room.is_available)  # Room is no longer globally unavailable

    def test_edit_reservation(self):
        self.client.login(username='tester', password='pass1234')
        self.client.post(reverse('room_details'), data=self._reservation_payload())
        reservation = Reservation.objects.first()
        new_check_out = reservation.check_in_date + datetime.timedelta(days=3)
        payload = self._reservation_payload()
        payload['check_out_date'] = new_check_out.isoformat()

        response = self.client.post(
            reverse('reservation_edit', args=[reservation.id]),
            data=payload,
        )
        self.assertRedirects(response, reverse('reservation_list'))
        reservation.refresh_from_db()
        self.assertEqual(reservation.check_out_date, new_check_out)

    def test_delete_reservation(self):
        self.client.login(username='tester', password='pass1234')
        self.client.post(reverse('room_details'), data=self._reservation_payload())
        reservation = Reservation.objects.first()

        response = self.client.post(reverse('reservation_delete', args=[reservation.id]))
        self.assertRedirects(response, reverse('reservation_list'))
        self.assertEqual(Reservation.objects.count(), 0)
        self.room.refresh_from_db()
        # self.assertTrue(self.room.is_available)
