// تأكيد الحذف قبل إرسال الفورم
document.addEventListener('DOMContentLoaded', function () {
    const deleteForms = document.querySelectorAll('form[action="/delete_product"]');
    deleteForms.forEach(function (form) {
        form.addEventListener('submit', function (e) {
            if (!confirm('هل أنت متأكد من حذف هذا المنتج؟')) {
                e.preventDefault();
            }
        });
    });

    // إخفاء رسائل التنبيه تلقائيًا بعد 4 ثواني
    const messages = document.querySelectorAll('.success, .error');
    messages.forEach(function (msg) {
        setTimeout(function () {
            msg.style.transition = 'opacity 0.5s ease';
            msg.style.opacity = '0';
            setTimeout(function () { msg.remove(); }, 500);
        }, 4000);
    });
});
