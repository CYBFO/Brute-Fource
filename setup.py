from setuptools import setup, find_packages

setup(
    name="brute_force_tool",         # اسم الأداة
    version="1.0.0",                 # رقم الإصدار
    description="أداة بروت فورس متعددة المهام",  # وصف قصير
    author="اسمك",                  # اسمك كمطور
    packages=find_packages(),        # العثور على الحزم (إذا كان هناك أكثر من ملف Python)
    entry_points={
        'console_scripts': [         # الأمر الذي سيُستخدم لتشغيل الأداة بعد التثبيت
            'bruteforce=brute_force_tool:main', 
        ],
    },
    install_requires=[],             # المكتبات المطلوبة (فارغ هنا إذا لم تستخدم مكتبات إضافية)
)
