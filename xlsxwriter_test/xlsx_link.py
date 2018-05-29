import xlsxwriter,time

# Create a new workbook and add a worksheet
# filename = time.strftime("%h-%m-%s",time.localtime())
workbook = xlsxwriter.Workbook('hyperlink_1.xlsx')
worksheet = workbook.add_worksheet('Hyperlinks')
worksheet_test = workbook.add_worksheet('Sheet_test')

worksheet_test.write(0,0,"test!")
worksheet_test.write(0,1,"Sheet2!A1:B2")
# Format the first column
worksheet.set_column('A:A', 30)

# Add a sample alternative link format.
red_format = workbook.add_format({
    'font_color': 'red',
    'bold':       1,
    'underline':  1,
    'font_size':  12,
})

# Write some hyperlinks
worksheet.write_url('A1', 'http://www.python.org/')  # Implicit format.
worksheet.write_url('A3', 'http://www.python.org/', string='Python Home')
worksheet.write_url('A5', 'http://www.python.org/', tip='Click here')
worksheet.write_url('A7', 'http://www.python.org/', red_format)
worksheet.write_url('A9', 'mailto:jmcnamara@cpan.org', string='Mail me')
worksheet.write_url('A10','internal:Sheet_test!A1',string="internal Sheet_test")
worksheet.write_url('A11', 'internal:Sheet2!A1:B2',string="Sheet2!A1:B2")

# Write a URL that isn't a hyperlink
worksheet.write_string('A11', 'http://www.python.org/')

workbook.close()
