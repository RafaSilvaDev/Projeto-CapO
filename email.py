# import win32com.client as win32
import win32com.client as win32

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'rafael.silva7@br.bosch.com'
mail.Subject = 'Message subject'
mail.Body = 'Message body'
mail.HTMLBody = '<h2>HTML Message body</h2>'

mail.Send()