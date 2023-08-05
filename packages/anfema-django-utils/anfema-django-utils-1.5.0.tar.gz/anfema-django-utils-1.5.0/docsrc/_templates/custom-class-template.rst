{{ fullname | escape | underline}}

.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}
   :members:
   :show-inheritance:
   :undoc-members:

   {% block methods %}
   {% if methods %}
   .. rubric:: {{ _('Methods') }}

   .. autosummary::
      :nosignatures:
   {% for item in methods %}
    {%- if item not in inherited_members %}
    {%- if not item.startswith('_') %}
     ~{{ name }}.{{ item }}
    {%- endif -%}
    {%- endif -%}
   {%- endfor %}
   {% endif %}
   {% endblock %}

   {% block attributes %}
   {% if attributes %}
   .. rubric:: {{ _('Attributes') }}

   .. autosummary::
   {% for item in attributes %}
    {%- if item not in inherited_members %}
    {%- if not item.startswith('_') %}
     ~{{ name }}.{{ item }}
    {% endif %}
    {% endif %}
   {%- endfor %}
   {% endif %}
   {% endblock %}
