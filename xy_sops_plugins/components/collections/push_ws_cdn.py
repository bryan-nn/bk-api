# -*- coding: utf-8 -*-

import logging

from django.utils.translation import ugettext_lazy as _

from pipeline.core.flow.activity import Service, StaticIntervalGenerator
from pipeline.component_framework.component import Component
from gcloud.conf import settings

logger = logging.getLogger('celery')
get_client_by_user = settings.ESB_GET_CLIENT_BY_USER

__group_name__ = _(u"轩辕游戏(XY_GAME)")


class PushWsCdnService(Service):
    __need_schedule__ = False

    def execute(self, data, parent_data):
        client = get_client_by_user(executor)

        test_textarea = data.inputs.test_textarea


        api_kwargs = {
            'text': test_textarea,
        }

        api_result = client.push_ws_cdn.push_wscdn(api_kwargs)
        

        if api_result['result']:
            data.set_outputs('data', api_result['result'])
            return True
        else:
            data.set_outputs('ex_data', api_result['result'])
            return False

    def outputs_format(self):
        return [
            self.OutputItem(name=_(u'结果数据'), key='data', type='string')
        ]


class PushWsCdnComponent(Component):
    name = _(u"推送网宿CDN")
    code = 'push_cdn'
    bound_service = PushWsCdn
    embedded_form = True
    form = """
    (function(){
        $.atoms.push_cdn = [
            {
                tag_code: "xy_game_plat",
                type: "textarea",
                attrs: {
                    name: gettext("平台"),
                    placeholder: gettext("平台名称"),
                    hookable: true,
                    validation: [
                        {
                            type: "required"
                        }
                    ]
                }
            },
            {
                tag_code: "xy_game_command",
                type: "input",
                attrs: {
                    name: gettext("参数"),
                    items：[
                        {value:'DOWNLOAD',name:"主包下载"},
                        {value:'SCDOWN',name:"渠道包下载"},
                        {value:'HOTFIX',name:"热更"},
                        {value:'GW_DOWN',name:"官网下载"},
                        {value:'GW_HOT',name:"官网热更"},
                    ],
                    placeholder: gettext("选择"),
                    hookable: true
                },
            },
            {
                tag_code: "xy_game_username",
                type: "input",
                attrs: {
                    name: gettext("API用户名"),
                    placeholder: gettext("可为空"),
                    hookable: true
                },
            },
            {
                tag_code: "xy_game_apikey",
                type: "input",
                attrs: {
                    name: gettext("APIKEY"),
                    placeholder: gettext("可为空"),
                    hookable: true
                },
            },

        ]
    })();
    """