import re
description = '''<description>&lt;img src="https://img.tyt.by/thumbnails/n/zamirovskiy/0f/2/anatoliy_glaz_20181025_zam_tutby_phsl_img_fo2a9145.jpg" width="72" height="48" alt="Фото: Вадим Замировский, TUT.BY" border="0" align="left" hspace="5" /&gt;- МИД направлена соответствующая нота российской стороне с просьбой прояснить ситуацию и уточнить, действительно ли изменен порядок пересечения границы, - рассказал Анатолий Глаз.&lt;br clear="all" /&gt;</description> '''

img_src = re.findall(r"&gt;(.+)&lt", description)[0]

print(img_src)
