"""
Test suite for Expense Tracker application.
"""

import pytest
from flask import Flask
from app import app


# ------------------------------------------------------------------ #
# Fixtures                                                            #
# ------------------------------------------------------------------ #

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# ------------------------------------------------------------------ #
# Landing Page Tests                                                    #
# ------------------------------------------------------------------ #

def test_landing_page(client):
    """Test that landing page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200


# ------------------------------------------------------------------ #
# Authentication Tests                                                  #
# ------------------------------------------------------------------ #

def test_register_page(client):
    """Test that register page loads successfully."""
    response = client.get('/register')
    assert response.status_code == 200


def test_login_page(client):
    """Test that login page loads successfully."""
    response = client.get('/login')
    assert response.status_code == 200


def test_logout_page(client):
    """Test that logout page loads successfully."""
    response = client.get('/logout')
    assert response.status_code == 200


# ------------------------------------------------------------------ #
# Profile Tests                                                       #
# ------------------------------------------------------------------ #

def test_profile_page(client):
    """Test that profile page loads successfully."""
    response = client.get('/profile')
    assert response.status_code == 200


# ------------------------------------------------------------------ #
# Expense Tests                                                       #
# ------------------------------------------------------------------ #

def test_add_expense_page(client):
    """Test that add expense page loads successfully."""
    response = client.get('/expenses/add')
    assert response.status_code == 200


def test_edit_expense_page(client):
    """Test that edit expense page loads for valid ID."""
    response = client.get('/expenses/1/edit')
    assert response.status_code == 200


def test_delete_expense_page(client):
    """Test that delete expense page loads for valid ID."""
    response = client.get('/expenses/1/delete')
    assert response.status_code == 200