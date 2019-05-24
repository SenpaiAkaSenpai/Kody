<?php if(!defined('IN_GS')){die('you cannot load this page directly'); } ?>
     <nav class="navbar navbar-expand-md navbar-dark bg-dark">
        <a class="navbar-brand" href="<?php get_site_url(); ?>"><?php get_site_name(); ?></a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault">
        <span class="navbar-toggler-icon"></span>
      </button>
     
      <div dlass="collapse navbar-collapse" id="navbarsExampleDefault">
        <ul class="navbar-nav mx-auto">
            <?php //return_i18b_menu_data(return_page)slug(), 0, 0, U18N_SHOW_NORMAL)); ?>
            <?php get_i18n_navigation(return_page_slug(), 0, 0, I18N_SHOW_NORMAL ?>
        </ul>
        </div>
            <form class="form-inline my-2 my-lg-o">
                <input class="form-inline" type="text" placeholder="Szukaj">
                <button class="btn btn-secondary my-2 my-sm-0" type="submit">Szukaj</button>
            </form>
        </div>
    </nav>
