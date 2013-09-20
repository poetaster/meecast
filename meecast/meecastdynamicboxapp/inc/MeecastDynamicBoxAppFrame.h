#ifndef _MeecastDynamicBoxApp_FRAME_H_
#define _MeecastDynamicBoxApp_FRAME_H_

#include <FApp.h>
#include <FBase.h>
#include <FSystem.h>
#include <FUi.h>
#include "../../core/config.h"

#include <FShell.h>

class MeecastDynamicBoxAppFrame
	: public Tizen::Shell::AppWidgetFrame
{
public:
	MeecastDynamicBoxAppFrame();
	virtual ~MeecastDynamicBoxAppFrame();
	virtual result OnInitializing(void);
	virtual result OnTerminating(void);
	virtual void OnBoundsChanged(const Tizen::Graphics::Rectangle& oldRect, const Tizen::Graphics::Rectangle& newRect);
	void OnAppWidgetUpdate(void);

private:
    Tizen::Ui::Controls::Panel* __pPanel;
	Tizen::Ui::Controls::Label* __pLabel;
    Tizen::Ui::Controls::Label* __pLabelBackground1;
    Tizen::Ui::Controls::Label* __pLabelBackground2;
    Tizen::Ui::Controls::Label* __pLabelBackgroundTown;
    Tizen::Ui::Controls::Label* __pLabelTown;
    Core::Config *_config;
};

#endif /* _MeecastDynamicBoxApp_FRAME_H_ */
