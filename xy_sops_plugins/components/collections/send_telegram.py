# -*- coding: utf-8 -*-

import logging

from django.utils.translation import ugettext_lazy as _

from pipeline.core.flow.activity import Service, StaticIntervalGenerator
from pipeline.component_framework.component import Component
from gcloud.conf import settings

logger = logging.getLogger('celery')
get_client_by_user = settings.ESB_GET_CLIENT_BY_USER

__group_name__ = _(u"轩辕游戏(XY_GAME)")


class TelegramCustomService(Service):
    __need_schedule__ = False

    def execute(self, data, parent_data):
        client = get_client_by_user(executor)

        test_textarea = data.inputs.test_textarea


        api_kwargs = {
            'text': test_textarea,
        }

        api_result = client.send_telegram.send_tele(api_kwargs)
        

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


class TelegramCustomComponent(Component):
    name = _(u"发送Telegram")
    code = 'telegram_custom'
    bound_service = TelegramCustom
    embedded_form = True
    form = """
    (function(){
        $.atoms.telegram_custom = [
            {
                tag_code: "telegram_textarea",
                type: "textarea",
                attrs: {
                    name: gettext("内容"),
                    placeholder: gettext("发送信息"),
                    hookable: true,
                    validation: [
                        {
                            type: "required"
                        }
                    ]
                }
            }
        ]
    })();
    """