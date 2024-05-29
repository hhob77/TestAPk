from simpledt import CSVDataTable
import speedtest
import sqlalchemy
import flet  as ft
import pandas as pd
import os
import csv



def main(page: ft.Page):
	page.scroll = "auto"
	# ===========================================
	# CSV
	csv = CSVDataTable("dataset.csv")
	xx = csv.datatable
	csv_res = ft.Row([xx],scroll="always")

	sp = speedtest.Speedtest()
	
	csv_file_path = 'dataset.csv'

	pdfile = pd.read_csv('dataset.csv')


	page.add(
	ft.Column([
	# NOW GET FROM CSV FILE AND INSERT TO datatable
	# I WANT TO DOWNLOAD THE FILE CSV
	ft.Text("GET FROM CSV FILE"),
	csv_res,
		])

	)

ft.app(target=main)
