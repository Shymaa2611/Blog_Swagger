# Blog_Swagger

steps :-
<p>1- install pyyaml and uritemplate</p>
<p>2- add this code in project/urls.py</p>
<pre>
from rest_framework.schemas import get_schema_view

urlpatterns = [
    # ...
    path('api_schema/', get_schema_view(
        title='API Schema',
        description='Guide for the REST API'
    ), name='api_schema'),
    # ...
]

</pre>
<p>http://127.0.0.1:8000/api_schema/</p>
<pre>
3-install Django Swagger module:
pip install django-rest-swagger
4- add 'rest_framework_swagger' to INSTALLED_APPS
5-create the HTML template file  documntation.html in templates/
</pre>
<!DOCTYPE html>
<html>
  <head>
    <title>School Service Documentation</title>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="//unpkg.com/swagger-ui-dist@3/swagger-ui.css" />
  </head>
  <body>
    <div id="swagger-ui"></div>
    <script src="//unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js"></script>
    <script>
    const ui = SwaggerUIBundle({
        url: "{% url schema_url %}",
        dom_id: '#swagger-ui',
        presets: [
          SwaggerUIBundle.presets.apis,
          SwaggerUIBundle.SwaggerUIStandalonePreset
        ],
        layout: "BaseLayout"
      })
    </script>
  </body>
</html>

<p>6- add  this code in project/urls.py</p>
<pre>
from django.views.generic import TemplateView

urlpatterns = [
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
]
</pre>
<p>http://127.0.0.1:8000/docs/</p>

![Alt Text](https://github.com/Shymaa2611/Blog_using_Swagger/assets/137145389/cd872a39-a8df-411f-ba3d-fe88871b2527)




















