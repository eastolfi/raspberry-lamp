import { LampPage } from './app.po';

describe('lamp App', () => {
  let page: LampPage;

  beforeEach(() => {
    page = new LampPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
