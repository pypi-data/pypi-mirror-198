import json
import importlib.resources as pkg_resources
from datetime import datetime

from pjplan import WBS


class DhtmlxTemplate:

    def __init__(self, name=None, file=None, data_placeholder="/*gant data here*/"):
        if not name and not file:
            raise RuntimeError("name or file should be not None")

        self.__template_name = name
        self.__template_file = file
        self.data_placeholder = data_placeholder

    def to_string(self, wbs: WBS):
        if self.__template_name:
            template = pkg_resources.read_text('pjplan.viz.dhtmlx.templates', self.__template_name + '.html')
        else:
            with open(self.__template_file, 'r', encoding='utf-8') as f:
                template = f.read()

        return template.replace(self.data_placeholder, self.gen_json(wbs))

    def to_file(self, wbs: WBS, file):
        v = self.to_string(wbs)
        with open(file, 'w', encoding='utf-8') as output:
            output.write(v)

    @staticmethod
    def gen_json(project: WBS, root_ids=None):

        if root_ids is None:
            roots = project.roots
        else:
            if type(root_ids) is int:
                root_ids = [root_ids]
            roots = [project(root_id) for root_id in root_ids]

        data = []
        links = []

        link_id = 0
        for _root in roots:
            for t in _root.all_children + [_root]:

                progress = 0
                if t.end < datetime.now():
                    progress = 1
                elif t.estimate > 0:
                    progress = 1 - (max(t.estimate - t.spent, 0))/t.estimate

                data_val = {
                    'id': t.id,
                    'text': t.name,
                    'type': 'milestone' if t.milestone else 'task',
                    'url': t.url if 'url' in t.__dict__ else t.name,
                    'start_date': t.start.strftime("%d-%m-%Y"),
                    'end_date': t.end.strftime("%d-%m-%Y"),
                    'resource': t.resource,
                    'open': t.id == _root.id,
                    'parent': t.parent.id if t.parent else 0,
                    'progress': progress,
                }

                data.append(data_val)

                for p in t.predecessors:
                    link_id += 1
                    links.append({
                        'id': link_id,
                        'source': p.id,
                        'target': t.id,
                        'type': "0"
                    })

        return json.dumps(
            {
                "data": data,
                "links": links
            },
            ensure_ascii=False,
            indent=2
        )