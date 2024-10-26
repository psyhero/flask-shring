document.addEventListener('DOMContentLoaded', () => {
    const btn_vtf = document.querySelector('#vertify');
    const message = document.querySelector('#error');
    const email = document.querySelector('[name="email"]');
    const username = document.querySelector('[name="username"]');

    btn_vtf.addEventListener('click', async (event) => {
        event.preventDefault();
        if (!email.value) {
            message.innerHTML = '请输入邮箱';
        } else {
            try {
                const response = await fetch(`/register/mail-vertify?email=${email.value}`);
                const result = await response.json();
                if (result['status'] == 200) {
                    message.innerHTML = result['message'];
                    btn_vtf.disabled = true;
                    let delta = 10;
                    const interval = setInterval(() => {
                        if (!delta) {
                            btn_vtf.disabled = false;
                            btn_vtf.innerHTML = '重新发送';
                            clearInterval(interval);
                        } else {
                            btn_vtf.innerHTML = `已发送(${delta}s)`;
                            delta -= 1;
                        }
                    }, 1000);
                } else if (result['status'] == 100) {
                    message.innerHTML = result['message'];
                    document.querySelector('#login').innerHTML = '去登录';
                } else {
                    message.innerHTML = result['message'];
                }
            } catch (err) {
                message.innerHTML = '错误：' + err.message;
            }
        }
    });

    username.addEventListener('input', async () => {
        try {
            const response = await fetch(`/register/username-vertify?username=${username.value}`);
            const result = await response.json();
            if (response.ok) {
                message.innerHTML = result['message'];
            } else {
                message.innerHTML = '请求失败，请重试';
            }
        } catch (err) {
            message.innerHTML = '错误：' + err.message;
        }
    });
});
