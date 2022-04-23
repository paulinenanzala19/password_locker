#!/usr/bin/env python3.6

from lock import User, Credentials

def create_user(username,password):
    """
    Function that creates a new user
    """
    new_user= User(username,password)
    return new_user

def save_users(user):
    """
    Function that saves the new users
    """
    user.save_user()

def verify_users():
    """
    Function that verifies incoming new users
    """
    user.verify_user()
