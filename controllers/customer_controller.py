from flask import Flask, render_template, request, redirect, Blueprint
from models.customer import Customer
import repositories.customer_repositories as customer_repositories
