/****************************************************************************
** Meta object code from reading C++ file 'qtwindow.hpp'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.12.8)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "Graphics/qtwindow.hpp"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'qtwindow.hpp' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.12.8. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
struct qt_meta_stringdata_AlgoWindow_t {
    QByteArrayData data[8];
    char stringdata0[83];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_AlgoWindow_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_AlgoWindow_t qt_meta_stringdata_AlgoWindow = {
    {
QT_MOC_LITERAL(0, 0, 10), // "AlgoWindow"
QT_MOC_LITERAL(1, 11, 13), // "buttonClicked"
QT_MOC_LITERAL(2, 25, 0), // ""
QT_MOC_LITERAL(3, 26, 7), // "checked"
QT_MOC_LITERAL(4, 34, 14), // "showMonteCarlo"
QT_MOC_LITERAL(5, 49, 11), // "varsChanged"
QT_MOC_LITERAL(6, 61, 10), // "setMaxDate"
QT_MOC_LITERAL(7, 72, 10) // "setMinDate"

    },
    "AlgoWindow\0buttonClicked\0\0checked\0"
    "showMonteCarlo\0varsChanged\0setMaxDate\0"
    "setMinDate"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_AlgoWindow[] = {

 // content:
       8,       // revision
       0,       // classname
       0,    0, // classinfo
       5,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    1,   39,    2, 0x08 /* Private */,
       4,    0,   42,    2, 0x08 /* Private */,
       5,    0,   43,    2, 0x08 /* Private */,
       6,    0,   44,    2, 0x08 /* Private */,
       7,    0,   45,    2, 0x08 /* Private */,

 // slots: parameters
    QMetaType::Void, QMetaType::Bool,    3,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void,

       0        // eod
};

void AlgoWindow::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        auto *_t = static_cast<AlgoWindow *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->buttonClicked((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->showMonteCarlo(); break;
        case 2: _t->varsChanged(); break;
        case 3: _t->setMaxDate(); break;
        case 4: _t->setMinDate(); break;
        default: ;
        }
    }
}

QT_INIT_METAOBJECT const QMetaObject AlgoWindow::staticMetaObject = { {
    &QWidget::staticMetaObject,
    qt_meta_stringdata_AlgoWindow.data,
    qt_meta_data_AlgoWindow,
    qt_static_metacall,
    nullptr,
    nullptr
} };


const QMetaObject *AlgoWindow::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *AlgoWindow::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_meta_stringdata_AlgoWindow.stringdata0))
        return static_cast<void*>(this);
    return QWidget::qt_metacast(_clname);
}

int AlgoWindow::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 5)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 5;
    }
    return _id;
}
QT_WARNING_POP
QT_END_MOC_NAMESPACE
