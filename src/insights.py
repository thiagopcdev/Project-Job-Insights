from src.jobs import read


def get_unique_job_types(path):
    get_jobs = read(path)
    type_list = []
    for job in get_jobs:
        if not job['job_type'] in type_list:
            type_list.append(job['job_type'])
    return type_list


def filter_by_job_type(jobs, job_type):
    get_jobs = jobs
    array_jobs = [
        job for job in get_jobs
        if job['job_type'] == job_type
        ]

    return array_jobs


def get_unique_industries(path):
    get_jobs = read(path)
    industry_list = []
    for job in get_jobs:
        if not job['industry'] in industry_list and job['industry']:
            industry_list.append(job['industry'])
    return industry_list


def filter_by_industry(jobs, industry):
    get_jobs = jobs
    array_industry = [
        job for job in get_jobs
        if job['industry'] == industry
        ]

    return array_industry


def get_max_salary(path):
    get_jobs = read(path)
    array_salary = [
        int(job['max_salary']) for job in get_jobs
        if job['max_salary'].isdigit()
        ]

    return max(array_salary)


def get_min_salary(path):
    get_jobs = read(path)
    array_salary = [
        int(job['min_salary']) for job in get_jobs
        if job['min_salary'].isdigit()
        ]

    return min(array_salary)


def salary_range_checks(job, salary):
    if('min_salary' not in job or not type(job['min_salary']) == int):
        return False
    if('max_salary' not in job or not type(job['max_salary']) == int):
        return False
    if(job['min_salary'] > job['max_salary']):
        return False
    if not (type(salary) == int):
        return False
    return True


def matches_salary_range(job, salary, raiser_enabled=True):
    if not salary_range_checks(job, salary):
        if raiser_enabled:
            raise ValueError
        else:
            return False
    if(job['min_salary'] <= salary <= job['max_salary']):
        return True
    return False


def filter_by_salary_range(jobs, salary):
    jobs_array = []
    for job in jobs:
        if (matches_salary_range(job, salary, raiser_enabled=False)):
            jobs_array.append(job)
    return jobs_array
