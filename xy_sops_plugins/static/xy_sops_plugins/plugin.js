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