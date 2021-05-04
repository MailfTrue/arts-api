from django.contrib import admin


class AdminSite(admin.AdminSite):
    site_title = "Административная панель"
    site_header = "Панель администратора"
    index_title = "Главная"


site = AdminSite()
