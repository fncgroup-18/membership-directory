from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.main import bp
from app.main.forms import CompanyForm, SearchForm
from app.models import Company

@bp.route('/')
@bp.route('/index')
def index():
    companies = Company.query.all()
    return render_template('main/index.html', title='Home', companies=companies)

@bp.route('/test')
def test():
    return "Hello! The application is running correctly!"

@bp.route('/company/new', methods=['GET', 'POST'])
@login_required
def create_company():
    if current_user.company:
        flash('You already have a registered company.')
        return redirect(url_for('main.index'))
    
    form = CompanyForm()
    if form.validate_on_submit():
        company = Company(
            name=form.name.data,
            description=form.description.data,
            industry=form.industry.data,
            website=form.website.data,
            address=form.address.data,
            phone=form.phone.data,
            owner=current_user
        )
        db.session.add(company)
        db.session.commit()
        flash('Your company has been registered!')
        return redirect(url_for('main.index'))
    return render_template('main/edit_company.html', title='Register Company', form=form)

@bp.route('/company/edit', methods=['GET', 'POST'])
@login_required
def edit_company():
    if not current_user.company:
        return redirect(url_for('main.create_company'))
    
    form = CompanyForm()
    if form.validate_on_submit():
        current_user.company.name = form.name.data
        current_user.company.description = form.description.data
        current_user.company.industry = form.industry.data
        current_user.company.website = form.website.data
        current_user.company.address = form.address.data
        current_user.company.phone = form.phone.data
        db.session.commit()
        flash('Your company details have been updated.')
        return redirect(url_for('main.index'))
    elif request.method == 'GET':
        form.name.data = current_user.company.name
        form.description.data = current_user.company.description
        form.industry.data = current_user.company.industry
        form.website.data = current_user.company.website
        form.address.data = current_user.company.address
        form.phone.data = current_user.company.phone
    return render_template('main/edit_company.html', title='Edit Company', form=form)

@bp.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        query = form.query.data
        companies = Company.query.filter(
            (Company.name.ilike(f'%{query}%')) |
            (Company.description.ilike(f'%{query}%')) |
            (Company.industry.ilike(f'%{query}%'))
        ).all()
        return render_template('main/search.html', title='Search Results', 
                             companies=companies, form=form)
    return render_template('main/search.html', title='Search', form=form)
